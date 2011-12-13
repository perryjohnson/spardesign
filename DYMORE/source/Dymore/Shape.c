#include "headerFiles.h"
#include "Shape.h"
#include "Curve.h"
#include "Iost.h"
#include "LcdType.h"
#include "LinearAlgebra.h"
#include "List.h"
#include "MemCtrl.h"
#include "MeshCurv.h"
#include "Model.h"
#include "NurbsC.h"
#include "NurbsS.h"
#include "Object.h"
#include "Surface.h"
#include "Table.h"

/*====================================================================*/
Shape ShapeCreate() {
  /*====================================================================*/
  Shape shape;
  /*-------------------------------*/
  /*  Allocate memory for a Shape  */
  /*-------------------------------*/
  shape = (Shape) MemCtrlAllocate(sizeof(OShape),64000);
  /*---------------------------*/
  /*  Initialize Shape fields  */
  /*---------------------------*/
  shape->object = ObjectCreate(64001,OBJ_SHAPE,WDY_MODEL,shape);
  shape->shptype = SHP_ANY; shape->lcdtype = SHP_ANY;
  shape->ListOfCurveNames = ListCreate(64009,LST_CHAR);
  shape->ListOfOrigins = ListCreate(64010,LST_TABLEITEM);
  shape->tableOfOrigins = NULL; shape->nbCurvesAtNodes = 0;
  shape->curvesAtUuu = shape->curvesAtNodes = NULL;
  shape->surfacesAtUuu = NULL;
  shape->nbPtOnNurbsU = shape->nbPtOnNurbsV = 0;

  return shape;
}

/*====================================================================*/
void ShapeDestroy 
(Shape shape /* pointer to Shape */ ) {
  /*====================================================================*/
  int i; Curve *curvesAtUuu, *curvesAtNodes; Surface *surfacesAtUuu;
  if (!shape) return;
  TableDestroy(ShapeGetTableOfOrigins(shape));
  if (curvesAtUuu = ShapeGetCurvesAtUuu(shape)) {
    for (i=0; i<ListGetLength(ShapeGetListOfCurveNames(shape)); i++)
      CurveDestroy(curvesAtUuu[i]);
    MemCtrlFree(curvesAtUuu);
  }
  if (curvesAtNodes = ShapeGetCurvesAtNodes(shape)) {
    for (i=0; i<ShapeGetNumberOfCurvesAtNodes(shape); i++)
      CurveDestroy(curvesAtNodes[i]);
    MemCtrlFree(curvesAtNodes);
  }
  if (surfacesAtUuu = ShapeGetSurfacesAtUuu(shape)) {
    for (i=0; i<ListGetLength(ShapeGetListOfCurveNames(shape)); i++)
      SurfaceDestroy(surfacesAtUuu[i]);
    MemCtrlFree(surfacesAtUuu);
  }
  ListEmptyAndDestroy(ShapeGetListOfCurveNames(shape));
  ListEmptyAndDestroy(ShapeGetListOfOrigins(shape));
  MemCtrlFree(shape);
}

/*====================================================================*/
Shape ShapeDuplicate
(Shape shpBase /* pointer to Shape  */ ) {
  /*====================================================================*/
  /*  Duplicates a shape                                                */
  /*====================================================================*/
  Shape shpDupl = ShapeCreate();
  /*--------------------*/
  /*  Duplicate Object  */
  /*--------------------*/
  ObjectDuplicate(ShapeGetObject(shpBase),ShapeGetObject(shpDupl),64002);
  /*------------------------*/
  /*  Duplicate definition  */
  /*------------------------*/
  ShapeSetShpType(shpDupl,ShapeGetShpType(shpBase));
  ShapeSetLcdType(shpDupl,ShapeGetLcdType(shpBase));
  ListDuplicate(ShapeGetListOfCurveNames(shpBase),
		ShapeGetListOfCurveNames(shpDupl),64004);
  ListDuplicate(ShapeGetListOfOrigins(shpBase),
		ShapeGetListOfOrigins(shpDupl),64005);
  ShapeSetNumberOfPointsOnNurbsU
    (shpDupl,ShapeGetNumberOfPointsOnNurbsU(shpBase));
  ShapeSetNumberOfPointsOnNurbsV
    (shpDupl,ShapeGetNumberOfPointsOnNurbsV(shpBase));
  
  return shpDupl;
}

/*====================================================================*/
void ShapeSetDefinitionType
(Shape shape, /* pointer to Shape */
 char *name   /* frame name       */ ) {
  /*====================================================================*/
  ShpType shptype = SHP_ANY;
  if      (SpellCheck(SPL_CURVE,  name)) shptype = SHP_CURVE;
  else if (SpellCheck(SPL_SURFACE,name)) shptype = SHP_SURFACE;
  else ShapeError(shape,ERR_SHAPE1,name,NULL);
  ShapeSetShpType(shape,shptype);
}

/*==============================================================*/
void ShapeRead
(Shape shape,    /* pointer to Shape  */
 char *dataFileN /* data file name    */ ) {
  /*==============================================================*/
  /*  Reads the definition of shapes                                    */
  /*====================================================================*/
  int iii; double eta, *YArray; char name[W_NAME]; TableItem tableitem;
  KeyType keyword, shpKey, lcdKey; LcdType lcdtype;
  /*-------------*/
  /*  Read name  */
  /*-------------*/
  ObjectReadDymName(ShapeGetObject(shape),64002,dataFileN);
  IostReadDymKeyWord(KEY_SHAPE,KEY_SHPTYP,NO);
  IostReadDymCharItem(KEY_SHAPE,name);
  ShapeSetDefinitionType(shape,name);
  switch (ShapeGetShpType(shape)) {
  case SHP_CURVE:   shpKey = KEY_CRVNAM;
    ShapeSetNumberOfPointsOnNurbsU(shape,20); break;
  case SHP_SURFACE: shpKey = KEY_SURNAM;
    ShapeSetNumberOfPointsOnNurbsU(shape,20);
    ShapeSetNumberOfPointsOnNurbsV(shape,20); break;
  }
  IostReadDymKeyWord(KEY_SHAPE,KEY_CODTYP,NO);
  IostReadDymCharItem(KEY_SHAPE,name);
  lcdtype = LcdTypeSetCoordinateType(name);
  if (lcdtype == LCD_ANY) {
    ShapeError(shape,ERR_SHAPE2,name,NULL); return;
  }
  else ShapeSetLcdType(shape,lcdtype);
  lcdKey = LcdTypeGetCoordinateKeyWord(lcdtype);
  /*---------------*/
  /*  Read shapes  */
  /*---------------*/
  while ((keyword = IostReadDymKeyWord(KEY_SHAPE,KEY_ANY,YES))
	 != KEY_CBRA) {
    switch (keyword) {
    case KEY_ETA: case KEY_SSS: case KEY_XXX:
      if (keyword == lcdKey) {
	IostReadDymDoubleArray(KEY_SHAPE,1,&eta);
	IostReadDymDelimiter(KEY_SHAPE,DEL_OBRA,NO);
	IostReadDymKeyWord(KEY_SHAPE,shpKey,NO);
	IostReadDymCharItem(KEY_SHAPE,name);
	ListAddItem(ShapeGetListOfCurveNames(shape),
		    StoreString(64003,name));
	tableitem = TableItemCreate(64005,eta,6);
	YArray = TableItemGetYArray(tableitem);
	IostReadDymKeyWord(KEY_SHAPE,KEY_SCAFAC,NO);
	IostReadDymDoubleArray(KEY_SHAPE,3,YArray  );
	IostReadDymKeyWord(KEY_SHAPE,KEY_ORIGIN,NO);
	IostReadDymDoubleArray(KEY_SHAPE,3,YArray+3);
	ListAddItem(ShapeGetListOfOrigins(shape),tableitem);
	IostReadDymDelimiter(KEY_SHAPE,DEL_CBRA,NO);
      }
      else ShapeError(shape,ERR_SHAPE9,NULL,NULL);
      break;
    case KEY_NBUPNT: IostReadDymIntegerArray(KEY_SHAPE,1,&iii);
      ShapeSetNumberOfPointsOnNurbsU(shape,iii);
      break;
    case KEY_NBVPNT: IostReadDymIntegerArray(KEY_SHAPE,1,&iii);
      ShapeSetNumberOfPointsOnNurbsV(shape,iii);
      break;
    default:
      IostErrorReadDym(IER_INPT12,KEY_SHAPE,
		       IostGetKeywordName(keyword),NULL);
      break;
    }
  }
  /*-------------------------*/
  /*  Echo shape definition  */
  /*-------------------------*/
  ShapeWriteOut(shape);
}

/*====================================================================*/
KeyType ShapeSetShpTypeCaption
(Shape shape,  /* pointer to Shape */
 char *caption /* caption for type  */ ) {
  /*====================================================================*/
  /*  Creates shape type caption                                        */
  /*====================================================================*/
  KeyType keyword; 
  caption[0] = '\0';
  switch (ShapeGetShpType(shape)) {
  case SHP_CURVE:   keyword = KEY_CRVNAM;
    strcat(caption,"CURVE");   break;
  case SHP_SURFACE: keyword = KEY_SURNAM;
    strcat(caption,"SURFACE"); break;
  }
  return keyword;
}

/*====================================================================*/
void ShapeWriteOut
(Shape shape /* pointer to Shape */ ) {
  /*====================================================================*/
  /*  Writes the definition of a shape to out file                      */
  /*====================================================================*/
  int iii; double eta, *YArray; char *name, caption[W_NAME];
  ListNode pres, pres1; TableItem tableitem; UntType unttype;

  IostWriteOutObjectName("Shape",ShapeGetName(shape));
  ShapeSetShpTypeCaption(shape,caption);
  IostWriteOutCharItem("Shape type",caption);
  unttype = LcdTypeGetCoordinateCaption(ShapeGetLcdType(shape),caption);
  IostWriteOutCharItem("Coordinate type",caption);
  if (ListGetLength(ShapeGetListOfCurveNames(shape)) > 0) {
    pres = ListGetHead(ShapeGetListOfCurveNames(shape));
    pres1 = ListGetHead(ShapeGetListOfOrigins(shape));
    while (name = (char*) ListNodeGetData(pres)) {
      tableitem = (TableItem) ListNodeGetData(pres1);
      YArray = TableItemGetYArray(tableitem);
      eta = TableItemGetXEntry(tableitem);
      IostWriteOutDoubleArray(caption,1,&eta,unttype,YES);
      switch (ShapeGetShpType(shape)) {
      case SHP_CURVE:
	IostWriteOutCharItem("Curve name",name); break;
      case SHP_SURFACE:
	IostWriteOutCharItem("Surface name",name); break;
      }
      IostWriteOutDoubleArray("Scaling factor",
			      3,YArray  ,UNT_ANY,YES);
      IostWriteOutDoubleArray("Origin",3,YArray+3,UNT_LENGTH,YES);
      pres = ListNodeGetNext(pres); pres1 = ListNodeGetNext(pres1);
    }
  }
  iii = ShapeGetNumberOfPointsOnNurbsU(shape);
  if ((iii != 0) && (iii != 20))
    IostWriteOutIntegerArray("Number of points on nurbs U",
			     1,&iii,YES);
  iii = ShapeGetNumberOfPointsOnNurbsV(shape);
  if ((iii != 0) && (iii != 20))
    IostWriteOutIntegerArray("Number of points on nurbs V",
			     1,&iii,YES);
}

/*====================================================================*/
void ShapeWriteDym
(Shape shape /* pointer to Shape */ ) {
  /*====================================================================*/
  /*  Writes the definition of a shape to dym file                      */
  /*====================================================================*/
  int iii; double eta, *YArray; char *name, caption[W_NAME];
  ListNode pres, pres1; TableItem tableitem; KeyType keyword;
  LcdType lcdtype = ShapeGetLcdType(shape);

  IostWriteDymObjectName(KEY_SHPNAM,ShapeGetName(shape));
  keyword = ShapeSetShpTypeCaption(shape,caption);
  IostWriteDymCharItem(KEY_SHPTYP,caption,YES);
  LcdTypeGetCoordinateCaption(lcdtype,caption);
  IostWriteDymCharItem(KEY_CODTYP,caption,YES);
  if (ListGetLength(ShapeGetListOfCurveNames(shape)) > 0) {
    pres = ListGetHead(ShapeGetListOfCurveNames(shape));
    pres1 = ListGetHead(ShapeGetListOfOrigins(shape));
    while (name = (char*) ListNodeGetData(pres)) {
      tableitem = (TableItem) ListNodeGetData(pres1);
      YArray = TableItemGetYArray(tableitem);
      eta = TableItemGetXEntry(tableitem);
      IostWriteDymDoubleArray
	(LcdTypeGetCoordinateKeyWord(lcdtype),1,&eta,YES);
      IostWriteDymOpenBrace();
      IostWriteDymCharItem(keyword,name,YES);
      IostWriteDymDoubleArray(KEY_SCAFAC,3,YArray  ,YES);
      IostWriteDymDoubleArray(KEY_ORIGIN,3,YArray+3,YES);
      IostWriteDymClosedBrace();
      pres = ListNodeGetNext(pres); pres1 = ListNodeGetNext(pres1);
    }
  }
  iii = ShapeGetNumberOfPointsOnNurbsU(shape);
  if (iii != 0 && iii != 20)
    IostWriteDymIntegerArray(KEY_NBUPNT,1,&iii,YES);
  iii = ShapeGetNumberOfPointsOnNurbsV(shape);
  if (iii != 0 && iii != 20)
    IostWriteDymIntegerArray(KEY_NBVPNT,1,&iii,YES);
  IostWriteDymClosedBrace();
}
/*====================================================================*/
void ShapeWriteHtm
(Shape shape /* pointer to Shape */ ) {
  /*====================================================================*/
  /*  Writes the definition of a shape to htm file                      */
  /*====================================================================*/
  int iii; double eta, *YArray; char *name, caption[W_NAME];
  ListNode pres, pres1; TableItem tableitem; KeyType keyword;
  LcdType lcdtype = ShapeGetLcdType(shape); UntType unttype;

  IostWriteHtmObjectHeading(ShapeGetObject(shape),
			    KEY_SHAPE,KEY_SHPNAM);
  keyword = ShapeSetShpTypeCaption(shape,caption);
  IostWriteHtmCharItem(KEY_SHPTYP,caption,NO);
  unttype = LcdTypeGetCoordinateCaption(ShapeGetLcdType(shape),caption);
  IostWriteHtmCharItem(KEY_CODTYP,caption,NO);
  if (ListGetLength(ShapeGetListOfCurveNames(shape)) > 0) {
    pres = ListGetHead(ShapeGetListOfCurveNames(shape));
    pres1 = ListGetHead(ShapeGetListOfOrigins(shape));
    while (name = (char*) ListNodeGetData(pres)) {
      tableitem = (TableItem) ListNodeGetData(pres1);
      YArray = TableItemGetYArray(tableitem);
      eta = TableItemGetXEntry(tableitem);
      IostWriteHtmDoubleArray
	(LcdTypeGetCoordinateKeyWord(lcdtype),1,&eta,unttype);
      IostWriteHtmCharItem(keyword,name,YES);
      IostWriteHtmDoubleArray(KEY_SCAFAC,3,YArray  ,UNT_ANY);
      IostWriteHtmDoubleArray(KEY_ORIGIN,3,YArray+3,UNT_LENGTH);
      pres = ListNodeGetNext(pres); pres1 = ListNodeGetNext(pres1);
    }
  }
  iii = ShapeGetNumberOfPointsOnNurbsU(shape);
  if (iii != 0 && iii != 20)
    IostWriteHtmIntegerArray(KEY_NBUPNT,1,&iii);
  iii = ShapeGetNumberOfPointsOnNurbsV(shape);
  if (iii != 0 && iii != 20)
    IostWriteHtmIntegerArray(KEY_NBVPNT,1,&iii);
  IostWriteHtmCloseDefinitionList();
}

/*====================================================================*/
void ShapeCheck
(Shape shape /* pointer to Shape */ ) {
  /*====================================================================*/
  /*  Checks the definition of shapes                                   */
  /*====================================================================*/
  int nbXEntry = ListGetLength(ShapeGetListOfOrigins(shape));
  int nbYEntry = 3; Table tableOfOrigins;
  /*-------------------*/
  /*  Write out shape  */
  /*-------------------*/
  ShapeWriteOut(shape);
  /*------------------------------*/
  /*  Construct table of origins  */
  /*------------------------------*/
  if (!nbXEntry) {
    ShapeError(shape,ERR_SHAPE4,NULL,NULL);
    return;
  }
  if (tableOfOrigins = ShapeGetTableOfOrigins(shape))
    TableDestroy(tableOfOrigins);
  ShapeSetTableOfOrigins(shape,tableOfOrigins = TableCreate());
  TableSetNames(tableOfOrigins,TBX_ETA,TBY_ORIGIN,
		ShapeGetName(shape));
  TableSetArrays(tableOfOrigins,nbXEntry,nbYEntry);
  TableStoreData(tableOfOrigins,ShapeGetListOfOrigins(shape));
  TableCheckOrderedTable(tableOfOrigins,ZERO,ONE);
  /*----------------*/
  /*  Check shapes  */
  /*----------------*/
  switch (ShapeGetShpType(shape)) {
  case SHP_CURVE:   ShapeCheckCurves(shape);   break;
  case SHP_SURFACE: ShapeCheckSurfaces(shape); break;
  }
}

/*====================================================================*/
void ShapeCheckCurves
(Shape shape /* pointer to Shape */ ) {
  /*====================================================================*/
  /*  Checks the definition of the curves of a shape                    */
  /*====================================================================*/
  int nbPt0, nbPtB, degree0, degreeB, ncp0, ncpB, ii, ic, ptNb, m;
  double *YArray, xx[4]; char *name;  ListNode pres, pres1;
  Curve curveB, curveN, *curvesAtUuu; TableItem tableitem;
  /*--------------------------*/
  /*  Allocate curves at uuu  */
  /*--------------------------*/
  ii = ListGetLength(ShapeGetListOfCurveNames(shape));
  curvesAtUuu = (Curve*) MemCtrlAllocate(ii*sizeof(Curve),64006);
  shape->curvesAtUuu = curvesAtUuu;
  for (m=0; m<ii; m++) curvesAtUuu[m] = NULL;
  /*--------------------*/
  /*  Loop over Curves  */
  /*--------------------*/
  nbPtB = degreeB = 0; ncpB = 3; ic = 0;
  pres = ListGetHead(ShapeGetListOfCurveNames(shape));
  pres1 = ListGetHead(ShapeGetListOfOrigins(shape));
  while (name = (char*) ListNodeGetData(pres)) {
    curveB = (Curve) GModelGetObjectData(name,OBJ_CURVE);
    if (curveB) {
      nbPtB = CurveGetNumberOfControlPoints(curveB);
      degreeB = CurveGetDegree(curveB); ncpB = CurveGetNcp(curveB);
      if (ic == 0) {
	nbPt0 = CurveGetNumberOfControlPoints(curveB);
	degree0 = CurveGetDegree(curveB); ncp0 = CurveGetNcp(curveB);
      }
      /*----------------------------------*/
      /*  Check curve control parameters  */
      /*----------------------------------*/
      if (nbPt0 != nbPtB)
	ShapeError(shape,ERR_SHAPE5,&nbPt0,&nbPtB);
      if (degree0 != degreeB)
	ShapeError(shape,ERR_SHAPE6,&degree0,&degreeB);
      if (ncp0 != ncpB) 
	ShapeError(shape,ERR_SHAPE7,&ncp0,&ncpB);
      /*--------------------*/
      /*  Create new curve  */
      /*--------------------*/
      curveN = CurveCreate(NO,WDY_NOWRITE); curvesAtUuu[ic] = curveN;
      CurveSetNumberOfControlPoints(curveN,nbPtB);
      CurveSetDegree(curveN,degreeB); CurveSetNcp(curveN,ncpB);
      CurveSetControlParameters(curveN,nbPtB,degreeB,ncpB==4);
      /*----------------------------------*/
      /*  Scale and shift control points  */
      /*----------------------------------*/
      tableitem = (TableItem) ListNodeGetData(pres1);
      YArray = TableItemGetYArray(tableitem);
      for (ptNb=0; ptNb<nbPtB; ptNb++) {
	CurveGetControlPoint(curveB,ptNb,xx);
	for (m=0; m<3; m++) xx[m] = YArray[m]*(xx[m] + YArray[m+3]);
	CurveSetControlPoint(curveN,ptNb,xx);
      }
      /*---------------------*/
      /*  Set knot sequence  */
      /*---------------------*/
      ALG_u0_v(CurveGetKnotSequence(curveN),
	       CurveGetKnotSequence(curveB),nbPtB+degreeB);
    }
    else ShapeError(shape,ERR_SHAPE3,name,NULL);
    pres = ListNodeGetNext(pres); pres1 = ListNodeGetNext(pres1); ic++;
  }
}

/*====================================================================*/
void ShapeCheckSurfaces
(Shape shape /* pointer to Shape */ ) {
  /*====================================================================*/
  /*  Checks the definition of the surfaces of a shape                  */
  /*====================================================================*/
  int nbPtUB, nbPtVB, degreeUB, degreeVB, ncpB, nbPtU0, nbPtV0;
  int degreeU0, degreeV0, ncp0, ptU, ptV, ii, ic, m;
  double *YArray, xx[4]; ListNode pres, pres1; TableItem tableitem;
  char *name; Surface surfaceB, surfaceN, *surfacesAtUuu;
  /*----------------------------*/
  /*  Allocate surfaces at uuu  */
  /*----------------------------*/
  ii = ListGetLength(ShapeGetListOfCurveNames(shape));
  surfacesAtUuu = (Surface*) MemCtrlAllocate
    (ii*sizeof(Surface),64007);
  shape->surfacesAtUuu = surfacesAtUuu;
  for (m=0; m<ii; m++) surfacesAtUuu[m] = NULL;
  /*----------------------*/
  /*  Loop over Surfaces  */
  /*----------------------*/
  nbPtUB = nbPtVB = degreeUB = degreeVB = 0; ncpB = 3; ic = 0;
  pres = ListGetHead(ShapeGetListOfCurveNames(shape));
  pres1 = ListGetHead(ShapeGetListOfOrigins(shape));
  while (name = (char*) ListNodeGetData(pres)) {
    surfaceB = (Surface) GModelGetObjectData(name,OBJ_SURFACE);
    if (surfaceB) {
      nbPtUB = SurfaceGetNumberOfControlPointsU(surfaceB);
      nbPtVB = SurfaceGetNumberOfControlPointsV(surfaceB);
      degreeUB = SurfaceGetDegreeU(surfaceB);
      degreeVB = SurfaceGetDegreeV(surfaceB);
      ncpB = SurfaceGetNcp(surfaceB);
      if (ic == 0) {
	nbPtU0 = nbPtUB; nbPtV0 = nbPtVB;
	degreeU0 = degreeUB; degreeV0 = degreeVB; ncp0 = ncpB;
      }
      /*----------------------------------*/
      /*  Check curve control parameters  */
      /*----------------------------------*/
      if (nbPtU0 != nbPtUB)
	ShapeError(shape,ERR_SHAPE5,&nbPtU0,&nbPtUB);
      if (nbPtV0 != nbPtVB)
	ShapeError(shape,ERR_SHAPE5,&nbPtV0,&nbPtVB);
      if (degreeU0 != degreeUB)
	ShapeError(shape,ERR_SHAPE6,&degreeU0,&degreeUB);
      if (degreeV0 != degreeVB)
	ShapeError(shape,ERR_SHAPE6,&degreeV0,&degreeVB);
      if (ncp0 != ncpB) 
	ShapeError(shape,ERR_SHAPE7,&ncp0,&ncpB);
      /*----------------------*/
      /*  Create new surface  */
      /*----------------------*/
      surfaceN = SurfaceCreate(NO,WDY_NOWRITE);
      surfacesAtUuu[ic] = surfaceN;
      SurfaceSetNumberOfControlPointsU(surfaceN,nbPtUB);
      SurfaceSetNumberOfControlPointsV(surfaceN,nbPtVB);
      SurfaceSetDegreeU(surfaceN,degreeUB);
      SurfaceSetDegreeV(surfaceN,degreeVB);
      SurfaceSetNcp(surfaceN,ncpB);
      SurfaceSetControlParameters(surfaceN);
      /*----------------------------------*/
      /*  Scale and shift control points  */
      /*----------------------------------*/
      tableitem = (TableItem) ListNodeGetData(pres1);
      YArray = TableItemGetYArray(tableitem);
      for (ptV=0; ptV<nbPtVB; ptV++) {
	for (ptU=0; ptU<nbPtUB; ptU++) {
	  SurfaceGetControlPoint(surfaceB,ptU,ptV,xx);
	  for (m=0; m<3; m++) xx[m] = YArray[m]*(xx[m] + YArray[m+3]);
	  SurfaceSetControlPoint(surfaceN,ptU,ptV,xx);
	}
      }
      /*---------------------*/
      /*  Set knot sequence  */
      /*---------------------*/
      ALG_u0_v(SurfaceGetKnotSequenceU(surfaceN),
	       SurfaceGetKnotSequenceU(surfaceB),nbPtUB+degreeUB+1);
      ALG_u0_v(SurfaceGetKnotSequenceV(surfaceN),
	       SurfaceGetKnotSequenceV(surfaceB),nbPtVB+degreeVB+1);
    }
    else ShapeError(shape,ERR_SHAPE8,name,NULL);
    pres = ListNodeGetNext(pres); pres1 = ListNodeGetNext(pres1); ic++;
  }
}

/*====================================================================*/
void ShapeError
(Shape shape,       /* pointer to Shape  */
 ErrShape errshape, /* error type        */
 void *item1,       /* pointer to item 1 */
 void *item2        /* pointer to item 2 */ ) {
  /*====================================================================*/
  /*  Handles Point errors                                              */
  /*====================================================================*/
  char *line1 = IostGetErrorLine1(), *line2 = IostGetErrorLine2();
  char *line3 = IostGetErrorLine3(), *line4 = IostGetErrorLine4();
  char *name = ShapeGetName(shape); char leg[2*W_NAME];
  /*------------------------*/
  /*  Set model error flag  */
  /*------------------------*/
  IostSetErrorFlag(YES,ShapeGetObject(shape));
  /*---------------------*/
  /*  Set error message  */
  /*---------------------*/
  sprintf(leg,"For shape [%s]",name);
  switch (errshape) {
  case ERR_SHAPE1: sprintf(line1,"Error: SHAPE1. %s",leg);
    sprintf(line2,"Unknown shape type: [%s]",(char *) item1);
    break;
  case ERR_SHAPE2: sprintf(line1,"Error: SHAPE2. %s",leg);
    sprintf(line2,"Unknown coordinate type: [%s]",(char*) item1);
    break;
  case ERR_SHAPE3: sprintf(line1,"Error: SHAPE3. %s",leg);
    sprintf(line2,"Curve: [%s]",(char *) item1);
    sprintf(line3,"does not exist.");
    break;
  case ERR_SHAPE4: sprintf(line1,"Error: SHAPE4. %s",leg);
    sprintf(line2,"No entries were defined for this shape.");
    break;
  case ERR_SHAPE5: sprintf(line1,"Error: SHAPE5. %s",leg);
    sprintf(line2,"The number of control points of all curves/surfaces");
    sprintf(line3,"in a shape definition must match.");
    sprintf(line4,"Number of control points: %5i, %5i",*(int *) item1,
	    *(int *) item2);
    break;
  case ERR_SHAPE6: sprintf(line1,"Error: SHAPE6. %s",leg);
    sprintf(line2,"The degree of all curves/surfaces in");
    sprintf(line3,"a shape definition must match.");
    sprintf(line4,"Degree: %5i, %5i",*(int *) item1,*(int *) item2);
    break;
  case ERR_SHAPE7: sprintf(line1,"Error: SHAPE7. %s",leg);
    sprintf(line2,"All curves/surfaces in shape definition must be");
    sprintf(line3,"non rational or rational. ncp: %5i, %5i",
	    *(int *) item1,*(int *) item2);
    break;
  case ERR_SHAPE8: sprintf(line1,"Error: SHAPE8. %s",leg);
    sprintf(line2,"Surface: [%s] does not exist.",(char *) item1);
    break;
  case ERR_SHAPE9: sprintf(line1,"Error: SHAPE9. %s",leg);
    sprintf(line2,"All shape entries must have");
    sprintf(line3,"the same coordinate definition");
    break;
  }
  /*-----------------------*/
  /*  Print error message  */
  /*-----------------------*/
  IostWriteOutErrorMessage(name);
}

/*====================================================================*/
void ShapeInterpolateCurves
(Shape shape,       /* pointer to Shape    */
 MeshCurv meshcurv  /* pointer to MeshCurv */ ) {
  /*====================================================================*/
  /*  Interpolates uuu curves to nodal curves                           */
  /*====================================================================*/
  int nbUuu, nbPt, noel, ncp, Rational, j, ic, in, ipos, degree;
  int nbOfElements = MeshCurvGetNumberOfElements(meshcurv);
  int odOfElements = MeshCurvGetOrderOfElements(meshcurv), nbCurvesAtNodes;
  Curve curve0, curveN, *curvesAtUuu = ShapeGetCurvesAtUuu(shape);
  Curve *curvesAtNodes; Table table = ShapeGetTableOfOrigins(shape);
  double eta, eta0, eta1, deta, hh, xb, aa, bb;
  double *XArray = TableGetXArray(table), *uuu = MeshCurvGetUuu(meshcurv);
  /*------------------*/
  /*  Allocate space  */
  /*------------------*/
  if (ShapeGetNumberOfCurvesAtNodes(shape)) return;
  nbUuu = ListGetLength(ShapeGetListOfCurveNames(shape));
  nbCurvesAtNodes = (nbUuu == 1)? 1: nbOfElements*odOfElements + 1;
  shape->nbCurvesAtNodes = nbCurvesAtNodes;
  curvesAtNodes = (Curve*) MemCtrlAllocate
    (nbCurvesAtNodes*sizeof(Curve),64008);
  shape->curvesAtNodes = curvesAtNodes;
  /*----------------------*/
  /*  Extract curve data  */
  /*----------------------*/
  curve0 = curvesAtUuu[0]; nbPt = CurveGetNumberOfControlPoints(curve0);
  degree = CurveGetDegree(curve0); ncp = CurveGetNcp(curve0);
  Rational = (ncp == 4)? YES: NO;
  /*----------------*/
  /*  Single curve  */
  /*----------------*/
  if (nbUuu == 1) {
    curveN = CurveCreate(NO,WDY_NOWRITE); curvesAtNodes[0] = curveN;
    CurveSetNumberOfControlPoints(curveN,nbPt);
    CurveSetDegree(curveN,degree); CurveSetNcp(curveN,ncp);
    CurveSetControlParameters(curveN,nbPt,degree,Rational);
    /*-----------------------*/
    /*  Copy control points  */
    /*-----------------------*/
    ALG_u0_v(CurveGetControlPointArray(curveN),
	     CurveGetControlPointArray(curve0),nbPt*ncp);
    /*----------------------*/
    /*  Copy knot sequence  */
    /*----------------------*/
    ALG_u0_v(CurveGetKnotSequence(curveN),
	     CurveGetKnotSequence(curve0),nbPt+degree+1);
  }
  /*-----------------------*/
  /*  Loop over bld nodes  */
  /*-----------------------*/
  else {
    eta0 = uuu[0];
    for (noel=ic=0; noel<nbOfElements; noel++) {
      eta1 = uuu[noel+1]; deta = (eta1 - eta0)/odOfElements;
      in = (noel == 0)? 0: 1;
      for (j=in; j<=odOfElements; j++) {
	eta = eta0 + j*deta;
	curveN = CurveCreate(NO,WDY_NOWRITE);
	curvesAtNodes[ic++] = curveN;
	CurveSetNumberOfControlPoints(curveN,nbPt);
	CurveSetDegree(curveN,degree); CurveSetNcp(curveN,ncp);
	CurveSetControlParameters(curveN,nbPt,degree,Rational);
	/*--------------------------------*/
	/*  Set interpolation parameters  */
	/*--------------------------------*/
	ipos = TableSearchOrderedTable(table,eta);
	hh = XArray[ipos+1] - XArray[ipos];
	xb = (eta - XArray[ipos]) / hh;
	bb = xb; aa = ONE - xb;
	/*------------------------------*/
	/*  Interpolate control points  */
	/*------------------------------*/
	ALG_u0_svpsw(CurveGetControlPointArray(curveN),
		     aa,CurveGetControlPointArray(curvesAtUuu[ipos  ]),
		     bb,CurveGetControlPointArray(curvesAtUuu[ipos+1]),
		     nbPt*ncp);
	/*-----------------------------*/
	/*  Interpolate knot sequence  */
	/*-----------------------------*/
	ALG_u0_svpsw(CurveGetKnotSequence(curveN),
		     aa,CurveGetKnotSequence(curvesAtUuu[ipos  ]),
		     bb,CurveGetKnotSequence(curvesAtUuu[ipos+1]),
		     nbPt+degree+1);
      }
      eta0 = eta1;
    }
  }
}
