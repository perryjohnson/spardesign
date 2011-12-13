#include "headerFiles.h"
#include "ViewParm.h"
#include "A3DLib.h"
#include "FiniteRotationLib.h"
#include "Iost.h"
#include "LinearAlgebra.h"
#include "MemCtrl.h"
#include "Object.h"

/*====================================================================*/
ViewParm ViewParmCreate() {
  /*====================================================================*/
  ViewParm viewparm;
  /*----------------------------------*/
  /*  Allocate memory for a ViewParm  */
  /*----------------------------------*/
  viewparm = (ViewParm) MemCtrlAllocate(sizeof(OViewParm),65000);
  /*------------------------------*/
  /*  Initialize ViewParm fields  */
  /*------------------------------*/
  viewparm->object = ObjectCreate(65001,OBJ_VIEWPARM,WDY_PST,viewparm);
  viewparm->readInDymFlag = NO;
  A3D_u0_0(ViewParmGetViewReferencePoint(viewparm));
  A3D_u0_0(ViewParmGetViewSize(viewparm));
  A3D_u0_0(ViewParmGetProjectionReferencePoint(viewparm));
  A3D_u0_0(ViewParmGetProjectionEyeVector(viewparm));
  A3D_u0_0(ViewParmGetProjectionUpVector(viewparm));
  ALG_u0_0(ViewParmGetProjectionViewPort(viewparm),4);
  ALG_u0_0(ViewParmGetRotationMatrix(viewparm),9);

  return viewparm;
}

/*====================================================================*/
void ViewParmDestroy 
(ViewParm viewparm /* pointer to ViewParm */ ) {
 /*====================================================================*/
  if (!viewparm) return;
  MemCtrlFree(viewparm);
}

/*====================================================================*/
void ViewParmRead
(ViewParm viewparm, /* pointer to ViewParm */
 char *dataFileN    /* data file name      */ ) {
  /*====================================================================*/
  /*  This routine reads the show parameters                            */
  /*====================================================================*/
  double *array; KeyType keyword;
  /*-------------*/
  /*  Read name  */
  /*-------------*/
  ObjectReadDymName(ViewParmGetObject(viewparm),65002,dataFileN);
  /*-----------------------------*/
  /*  Read graphical parameters  */
  /*-----------------------------*/
  ViewParmSetReadInDymFileFlag(viewparm,NO);
  while ((keyword=IostReadDymKeyWord(KEY_VWPARM,KEY_ANY,YES))
	 != KEY_CBRA ) {
    switch (keyword) {
    case KEY_VWPRFP: array = ViewParmGetViewReferencePoint(viewparm);
      IostReadDymDoubleArray(KEY_VWPARM,3,array);
      ViewParmSetReadInDymFileFlag(viewparm,YES);
      break;
    case KEY_VWPSIZ: array = ViewParmGetViewSize(viewparm);
      IostReadDymDoubleArray(KEY_VWPARM,3,array);
      ViewParmSetReadInDymFileFlag(viewparm,YES);
      break;
    case KEY_VWPPRP: array = ViewParmGetProjectionReferencePoint(viewparm);
      IostReadDymDoubleArray(KEY_VWPARM,3,array);
      ViewParmSetReadInDymFileFlag(viewparm,YES);
      break;
    case KEY_VWPPEV: array = ViewParmGetProjectionEyeVector(viewparm);
      IostReadDymDoubleArray(KEY_VWPARM,3,array);
      ViewParmSetReadInDymFileFlag(viewparm,YES);
      break;
    case KEY_VWPPUV: array = ViewParmGetProjectionUpVector(viewparm);
      IostReadDymDoubleArray(KEY_VWPARM,3,array);
      ViewParmSetReadInDymFileFlag(viewparm,YES);
      break;
    case KEY_VWPPVP: array = ViewParmGetProjectionViewPort(viewparm);
      IostReadDymDoubleArray(KEY_VWPARM,4,array);
      ViewParmSetReadInDymFileFlag(viewparm,YES);
      break;
    default: IostErrorReadDym(IER_INPT12,KEY_VWPARM,
			      IostGetKeywordName(keyword),NULL);
    break;
    }
  }
  /*----------------------*/
  /*  Write Out ViewParm  */
  /*----------------------*/
  ViewParmWriteOut(viewparm);
}

/*====================================================================*/
void ViewParmWriteOut
(ViewParm viewparm /* pointer to ViewParm */ ) {
  /*==================================================================*/
  /*  Writes a viewparm to out file                                   */
  /*==================================================================*/
  double *array;
  IostWriteOutObjectName("View parameters definition",
			 ViewParmGetName(viewparm));
  array = ViewParmGetViewReferencePoint(viewparm);
  IostWriteOutDoubleArray("View reference point",
			  3,array,UNT_ANY,YES);
  array = ViewParmGetViewSize(viewparm);
  IostWriteOutDoubleArray("View size",3,array,UNT_ANY,YES);
  array = ViewParmGetProjectionReferencePoint(viewparm);
  IostWriteOutDoubleArray("Projection reference point",
			  3,array,UNT_ANY,YES);
  array = ViewParmGetProjectionEyeVector(viewparm);
  IostWriteOutDoubleArray("Projection eye vector",
			  3,array,UNT_ANY,YES);
  array = ViewParmGetProjectionUpVector(viewparm);
  IostWriteOutDoubleArray("Projection up vector",
			  3,array,UNT_ANY,YES);
  array = ViewParmGetProjectionViewPort(viewparm);
  IostWriteOutDoubleArray("Projection viewport",
			  4,array,UNT_ANY,YES);
}

/*====================================================================*/
void ViewParmWriteDym
(ViewParm viewparm /* pointer to ViewParm */ ) {
  /*====================================================================*/
  /*  Writes a viewparm to dym file                                     */
  /*====================================================================*/
  double *array;
  IostWriteDymObjectName(KEY_VWPNAM,ViewParmGetName(viewparm));
  /*---------------------------*/
  /*  Skip if not initialized  */
  /*---------------------------*/
  array = ViewParmGetViewSize(viewparm);
  if (array[0] == ZERO && array[1] == ZERO && array[2] == ZERO) return;
  array = ViewParmGetProjectionViewPort(viewparm);
  if (array[0] == ZERO && array[1] == ZERO &&
      array[2] == ZERO && array[3] == ZERO) return;

  array = ViewParmGetViewReferencePoint(viewparm);
  IostWriteDymDoubleArray(KEY_VWPRFP,3,array,YES);
  array = ViewParmGetViewSize(viewparm);
  IostWriteDymDoubleArray(KEY_VWPSIZ,3,array,YES);
  array = ViewParmGetProjectionReferencePoint(viewparm);
  IostWriteDymDoubleArray(KEY_VWPPRP,3,array,YES);
  array = ViewParmGetProjectionEyeVector(viewparm);
  IostWriteDymDoubleArray(KEY_VWPPEV,3,array,YES);
  array = ViewParmGetProjectionUpVector(viewparm);
  IostWriteDymDoubleArray(KEY_VWPPUV,3,array,YES);
  array = ViewParmGetProjectionViewPort(viewparm);
  IostWriteDymDoubleArray(KEY_VWPPVP,4,array,YES);
  IostWriteDymClosedBrace();
}

/*====================================================================*/
void ViewParmWriteHtm
(ViewParm viewparm /* pointer to ViewParm */ ) {
  /*====================================================================*/
  /*  Writes a viewparm to htm file                                     */
  /*====================================================================*/
  double *array;
  IostWriteHtmObjectHeading(ViewParmGetObject(viewparm),
			    KEY_VWPARM,KEY_VWPNAM);
  array = ViewParmGetViewReferencePoint(viewparm);
  IostWriteHtmDoubleArray(KEY_VWPRFP,3,array,UNT_ANY);
  array = ViewParmGetViewSize(viewparm);
  IostWriteHtmDoubleArray(KEY_VWPSIZ,3,array,UNT_ANY);
  array = ViewParmGetProjectionReferencePoint(viewparm);
  IostWriteHtmDoubleArray(KEY_VWPPRP,3,array,UNT_ANY);
  array = ViewParmGetProjectionEyeVector(viewparm);
  IostWriteHtmDoubleArray(KEY_VWPPEV,3,array,UNT_ANY);
  array = ViewParmGetProjectionUpVector(viewparm);
  IostWriteHtmDoubleArray(KEY_VWPPUV,3,array,UNT_ANY);
  array = ViewParmGetProjectionViewPort(viewparm);
  IostWriteHtmDoubleArray(KEY_VWPPVP,4,array,UNT_ANY);
  IostWriteHtmCloseDefinitionList();
}

/*====================================================================*/
void ViewParmInitialize
(ViewParm viewparm, /* pointer to ViewParm   */
 float *vmin,       /* minimum coordinates   */
 float *vmax,       /* maximum coordinates   */
 float aspectRatio  /* viewport aspect ratio */ ) {
  /*====================================================================*/
  /*  Initialize view parameters                                        */
  /*====================================================================*/
  int i; double tr1, tr2, maxSize = ZERO; 
  double *viewSize = ViewParmGetViewSize(viewparm);
  double *viewRefPoint = ViewParmGetViewReferencePoint(viewparm);
  double *projViewPort = ViewParmGetProjectionViewPort(viewparm);
  /*-----------------------------------------*/
  /*  Compute view reference point and size  */
  /*-----------------------------------------*/
  for (i=0; i<3; i++) {
    tr1 = vmin[i]; tr2 = vmax[i];
    viewRefPoint[i] = HALF*(tr1 + tr2);
    viewSize[i] = tr2 - tr1;
    if (viewSize[i] > maxSize) maxSize = viewSize[i];
  }
  viewSize[0] = viewSize[1] = viewSize[2] = 1.2*maxSize;
  /*-------------------------------*/
  /*  Set orthographic projection  */
  /*-------------------------------*/
  projViewPort[0] = projViewPort[2] = - ONE;
  projViewPort[1] = projViewPort[3] =   ONE;
  /*----------------------------------*/
  /*  Take care of the window aspect  */
  /*----------------------------------*/
  if (aspectRatio > ONE) {
    projViewPort[0] = - aspectRatio; projViewPort[1] = aspectRatio;}
  else {
    projViewPort[2] = - ONE/aspectRatio; projViewPort[3] = ONE/aspectRatio;}
  /*---------------------------------*/
  /*  Set reference point at origin  */
  /*---------------------------------*/
  A3D_u0_0(ViewParmGetProjectionReferencePoint(viewparm));
  /*------------------------------*/
  /*  Set view orientation to XY  */
  /*------------------------------*/
  ViewParmSetViewOrientation(viewparm,0);
}

/*====================================================================*/
void ViewParmSetViewOrientation
(ViewParm viewparm, /* pointer to ViewParm */
 int flag           /* orientation flag    */ ) { 
  /*====================================================================*/
  /*  Sets standard eye vector direction. Orientation flag = 0, 1, 2    */
  /*                                         eye direction = z, x, y    */
  /*====================================================================*/
  int up, eye;
  double *projUpVector = ViewParmGetProjectionUpVector(viewparm);
  double *projEyeVector = ViewParmGetProjectionEyeVector(viewparm);
  /*---------------------*/
  /*  Compute up vector  */
  /*---------------------*/
  up = flag + 1; if (up > 2) up  -= 3;
  A3D_u0_0(projUpVector); projUpVector[up] = ONE;
  /*----------------------*/
  /*  Compute eye vector  */
  /*----------------------*/
  eye = flag + 2; if (eye > 2) eye -= 3;
  A3D_u0_0(projEyeVector); projEyeVector[eye] = ONE;
  /*---------------------------*/
  /*  Compute rotation matrix  */
  /*---------------------------*/
  ViewParmComputeRotationMatrix(viewparm);
}

/*====================================================================*/
void ViewParmComputeRotationMatrix
(ViewParm viewparm /* pointer to ViewParm */ ) {
  /*====================================================================*/
  double *Rr = ViewParmGetRotationMatrix(viewparm);
  /*---------------------------*/
  /*  Compute rotation matrix  */
  /*---------------------------*/
  A3D_u0_v(Rr+6,ViewParmGetProjectionEyeVector(viewparm));
  A3D_u0_v(Rr+3,ViewParmGetProjectionUpVector(viewparm));
  A3D_u0_vSw(Rr,Rr+3,Rr+6);
}

/*====================================================================*/
float ViewParmGetScale
(ViewParm viewparm /* pointer to ViewParm */ ) {
  /*====================================================================*/
  double px, py, *projViewPort = ViewParmGetProjectionViewPort(viewparm);
  /*------------------------------------------*/
  /*  Compute scale wrt projection view port  */
  /*------------------------------------------*/
  px = projViewPort[1] - projViewPort[0];
  py = projViewPort[3] - projViewPort[2];
  return (float) ((px > py)? py: px);
}

/*====================================================================*/
void ViewParmIncrementOrientationMatrix
(ViewParm viewparm, /* pointer to ViewParm               */
 float phi1,        /* incremental rotation about 1 axis */
 float phi2,        /* incremental rotation about 2 axis */
 float phi3         /* incremental rotation about 3 axis */) {
  /*====================================================================*/
  double tgphi[3], cc[3], Ri[9], Wrk[9];
  double *Rr = ViewParmGetRotationMatrix(viewparm);
  /*--------------------------------*/
  /*  Compute incremental rotation  */
  /*--------------------------------*/
  tgphi[1] = tan(phi1*PI); tgphi[0] = tan(phi2*PI); tgphi[2] = tan(phi3*PI);
  A3D_u0_Av(cc,Rr,tgphi); CrvMatrixR(cc,Ri);
  /*-----------------------*/
  /*  Set new orientation  */
  /*-----------------------*/
  A3D_A0_BC(Wrk,Ri,Rr); ALG_u0_v(Rr,Wrk,9);
  /*-----------------------------*/
  /*  Set projection eye vector  */
  /*-----------------------------*/
  A3D_u0_v(ViewParmGetProjectionEyeVector(viewparm),Rr+6);
  /*----------------------------*/
  /*  Set projection up vector  */
  /*----------------------------*/
  A3D_u0_v(ViewParmGetProjectionUpVector(viewparm),Rr+3);
}

/*====================================================================*/
void ViewParmTranslateProjectionReferencePoint
(ViewParm viewparm, /* pointer to ViewParm              */
 float dx,          /* reference point translation in x */
 float dy           /* reference point translation in y */ ) {
  /*====================================================================*/
  double tr[3], *projViewPort = ViewParmGetProjectionViewPort(viewparm);
  tr[0] = - dx*(projViewPort[1] - projViewPort[0]);
  tr[1] = - dy*(projViewPort[3] - projViewPort[2]);
  tr[2] = ZERO;
  A3D_u1_Av(ViewParmGetProjectionReferencePoint(viewparm),
	    ViewParmGetRotationMatrix(viewparm),tr);
}

/*=============================================================*/
void ViewParmResizeProjectionViewPort
(ViewParm viewparm, /* pointer to ViewParm */
 float dsize        /* scaling factor      */ ) {
  /*==============================================================*/
  double tr1, tr2, *projViewPort = ViewParmGetProjectionViewPort(viewparm);
  tr1 = HALF*dsize*(projViewPort[1] - projViewPort[0]);
  projViewPort[0] -= tr1;  projViewPort[1] += tr1;
  tr2 = HALF*dsize*(projViewPort[3] - projViewPort[2]);
  projViewPort[2] -= tr2;  projViewPort[3] += tr2;
}

/*====================================================================*/
void ViewParmUpdateProjectionViewport
(ViewParm viewparm, /* pointer to ViewParm */
 float aspectRatio  /* aspect ratio        */ ) {
  /*====================================================================*/
  /* Update projection viewport to preserve aspect ratio                */
  /*====================================================================*/
  double tr, *projViewPort = ViewParmGetProjectionViewPort(viewparm);
  if (aspectRatio == 0.0f) return;
  tr = (projViewPort[1] - projViewPort[0])/
       (projViewPort[3] - projViewPort[2])/aspectRatio;
  if (tr < ONE) {projViewPort[0] /= tr; projViewPort[1] /= tr;}
  else          {projViewPort[2] *= tr; projViewPort[3] *= tr;}
}

/*====================================================================*/
void ViewParmUpdateParallel
(ViewParm viewparm, /* pointer to ViewParm */
 float *minmax      /* Min max coordinates */ ) {
  /*====================================================================*/
  /* Update projection reference point for parallel projection          */
  /*====================================================================*/
  int i; double tr[3], ctp[3], pr;
  /*------------------*/
  /*  Compute center  */
  /*------------------*/
  for (i=0; i<3; i++) tr[i] = HALF*(minmax[i] + minmax[i+3]);
  A3D_u0_Av(ctp,ViewParmGetRotationMatrix(viewparm),tr);
  /*-----------------------------------------------*/
  /*  Projection of relative center on eye vector  */
  /*-----------------------------------------------*/
  pr = A3D_s0_uTv(ViewParmGetProjectionEyeVector(viewparm),ctp);
  /*----------------------------------------*/
  /*  Update eye-ray coordinate of proj_rp  */
  /*----------------------------------------*/
  A3D_u1_sv(ViewParmGetProjectionReferencePoint(viewparm),pr,
	    ViewParmGetProjectionEyeVector(viewparm));
}
