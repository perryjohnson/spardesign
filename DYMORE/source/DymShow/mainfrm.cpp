// MainFrm.cpp : implementation of the CMainFrame class
//

#include "stdafx.h"
#include "DymShow.h"

#include "MainFrm.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

////////////////////////////////////////////////////////
// CMainFrame

IMPLEMENT_DYNCREATE(CMainFrame, CFrameWnd)

BEGIN_MESSAGE_MAP(CMainFrame, CFrameWnd)
//{{AFX_MSG_MAP(CMainFrame)
ON_WM_CREATE()
ON_COMMAND(ID_VIEW_DYNAMICSTOOLBAR, OnViewDynamicstoolbar)
ON_COMMAND(ID_VIEW_STATICSTOOLBAR, OnViewStaticstoolbar)
ON_COMMAND(ID_VIEW_GRAPHICSTOOLBAR, OnViewGraphicstoolbar)
//}}AFX_MSG_MAP
END_MESSAGE_MAP()

static UINT indicators[] =
{
  ID_SEPARATOR,           // status line indicator
//    ID_INDICATOR_CAPS,
//    ID_INDICATOR_NUM,
//    ID_INDICATOR_SCRL,
};

//////////////////////////////////////////////////////
// CMainFrame construction/destruction

/*====================================================================*/
CMainFrame::CMainFrame() {
  /*====================================================================*/
}

/*=========================================================*/
CMainFrame::~CMainFrame() {
  /*=====================================================*/
}

/*=================================================*/
int CMainFrame::OnCreate
  (LPCREATESTRUCT lpCreateStruct) {
  /*====================================================================*/
  if (CFrameWnd::OnCreate(lpCreateStruct) == -1)
    return -1;
  /*---------------------------*/
  /*  Create Windows tool bar  */
  /*---------------------------*/  
  if (!m_wndToolBar.CreateEx(this, TBSTYLE_FLAT, WS_CHILD | WS_VISIBLE |
			     CBRS_TOP | CBRS_GRIPPER | CBRS_TOOLTIPS |
			     CBRS_FLYBY | CBRS_SIZE_DYNAMIC) ||
      !m_wndToolBar.LoadToolBar(IDR_MAINFRAME)) {
    TRACE0("Failed to create toolbar\n");
    return -1;      // fail to create
  }
  /*----------------------------*/
  /*  Create Dynamics tool bar  */
  /*----------------------------*/  
  if (!m_wndDynamicBar.CreateEx
      (this,TBSTYLE_FLAT,WS_CHILD | CBRS_TOP | CBRS_GRIPPER |
       CBRS_TOOLTIPS | CBRS_FLYBY | CBRS_SIZE_DYNAMIC) ||
      !m_wndDynamicBar.LoadToolBar(IDR_DYN)) {
    TRACE0("Failed to create dynamics toolbar\n");
    return -1;      // fail to create
  }
  /*---------------------------*/
  /*  Create Statics tool bar  */
  /*---------------------------*/  
  if (!m_wndStaticBar.CreateEx
      (this,TBSTYLE_FLAT,WS_CHILD | CBRS_TOP | CBRS_GRIPPER |
       CBRS_TOOLTIPS | CBRS_FLYBY | CBRS_SIZE_DYNAMIC) ||
      !m_wndStaticBar.LoadToolBar(IDR_STA)) {
    TRACE0("Failed to create statics toolbar\n");
    return -1;      // fail to create
  }
  /*----------------------------*/
  /*  Create Graphics tool bar  */
  /*----------------------------*/  
  if (!m_wndGraphicsBar.CreateEx
      (this,TBSTYLE_FLAT,WS_CHILD | CBRS_RIGHT | CBRS_GRIPPER |
       CBRS_TOOLTIPS | CBRS_FLYBY | CBRS_SIZE_DYNAMIC) ||
      !m_wndGraphicsBar.LoadToolBar(IDR_GRAPHICS)) {
    TRACE0("Failed to create graphics toolbar\n");
    return -1;      // fail to create
  }
  /*--------------------------*/
  /*  Create time status bar  */
  /*--------------------------*/
  if (!m_TimeStatusBar.Create(this) ||
      !m_TimeStatusBar.SetIndicators
      (indicators,sizeof(indicators)/sizeof(UINT))) {
    TRACE0("Failed to create time status bar\n");
    return -1;      // fail to create
  }
  /*------------------*/
  /*  Dock tool bars  */
  /*------------------*/  
  m_wndToolBar.EnableDocking(CBRS_ALIGN_ANY);
  m_wndDynamicBar.EnableDocking(CBRS_ALIGN_ANY);
  m_wndStaticBar.EnableDocking(CBRS_ALIGN_ANY);
  m_wndGraphicsBar.EnableDocking(CBRS_ALIGN_ANY);
  EnableDocking(CBRS_ALIGN_ANY);
  DockControlBar(&m_wndToolBar);
  DockControlBar(&m_wndDynamicBar);
  DockControlBar(&m_wndStaticBar);
  DockControlBar(&m_wndGraphicsBar);
  /*---------------------------------*/
  /*  Set menu checks for tool bars  */
  /*---------------------------------*/
  GetMenu()->CheckMenuItem(ID_VIEW_DYNAMICSTOOLBAR,MF_UNCHECKED);
  GetMenu()->CheckMenuItem(ID_VIEW_STATICSTOOLBAR,MF_UNCHECKED);
  GetMenu()->CheckMenuItem(ID_VIEW_GRAPHICSTOOLBAR,MF_UNCHECKED);
  /*----------------------------*/
  /*  Set StatusBar indicators  */
  /*----------------------------*/
  m_TimeStatusBar.SetTimeStatusBarTextWidth();
  ClearTimeStatusBarData();
  
  return 0;
}
 
/*====================================================================*/
BOOL CMainFrame::PreCreateWindow
  (CREATESTRUCT& cs) {
  /*====================================================================*/
  if( !CFrameWnd::PreCreateWindow(cs) ) return FALSE;
  // TODO: Modify the Window class or styles here by modifying
  //  the CREATESTRUCT cs
  
  return TRUE;
}
 
/*====================================================================*/
void CMainFrame::OnViewDynamicstoolbar() {
/*====================================================================*/
  /*------------------------------*/
  /*  Show/Hide dynamics toolbar  */
  /*------------------------------*/
  ChangeToolBarStatus(1,3);
}

/*====================================================================*/
void CMainFrame::OnViewStaticstoolbar() {
/*====================================================================*/
  /*-----------------------------*/
  /*  Show/Hide statics toolbar  */
  /*-----------------------------*/
  ChangeToolBarStatus(2,3);
}

/*====================================================================*/
void CMainFrame::OnViewGraphicstoolbar() {
/*====================================================================*/
  /*------------------------------*/
  /*  Show/Hide graphics toolbar  */
  /*------------------------------*/
  ChangeToolBarStatus(0,3);
}

/*====================================================================*/
void CMainFrame::ChangeToolBarStatus
(int toolBarType, /* tool bar type */
 int actionFlag   /* action flag   */ ) {
  /*====================================================================*/
  /* action flag value: 1 -> show; 2 -> hide; 3 -> toggle the tool bar  */
  /* toolBarType value: 0 -> graphics toolbar; 1 -> show toolbar        */
  /*                    2 -> eigen mode bar                             */
  /*====================================================================*/
  int id = 0;  UINT mstate;  BOOL status; CToolBar *toolbar;
  /*------------------*/
  /*  Select toolbar  */
  /*------------------*/
  switch (toolBarType) {
  case 0: id = ID_VIEW_GRAPHICSTOOLBAR;
    toolbar = &m_wndGraphicsBar; break;
  case 1: id = ID_VIEW_DYNAMICSTOOLBAR;
    toolbar = &m_wndDynamicBar; break;
  case 2: id = ID_VIEW_STATICSTOOLBAR;
    toolbar = &m_wndStaticBar; break;
  }
  /*-------------------------*/
  /*  Select desired status  */
  /*-------------------------*/
  switch (actionFlag) {
    /*-----------------*/
    /*  Show tool bar  */
    /*-----------------*/
  case 1: mstate = MF_CHECKED; status = TRUE;
    break;
    /*-----------------*/
    /*  Hide tool bar  */
    /*-----------------*/
  case 2: mstate = MF_UNCHECKED; status = FALSE;
    break;
    /*-------------------*/
    /*  Toggle tool bar  */
    /*-------------------*/
  case 3: 
    /*-----------------------------------*/
    /*  Get menu item check mark status  */
    /*-----------------------------------*/
    mstate = GetMenu()->CheckMenuItem(id,TRUE);
    /*------------------------*/
    /*  Reverse check status  */
    /*------------------------*/
    if (mstate == MF_CHECKED) {mstate = MF_UNCHECKED; status = FALSE;}
    else                      {mstate = MF_CHECKED;   status = TRUE; }
    break;
  }
  /*--------------------------------*/
  /*  Set/Unset check mark in menu  */
  /*--------------------------------*/
  GetMenu()->CheckMenuItem(id,mstate);
  /*---------------------*/
  /*  Show/Hide toolbar  */
  /*---------------------*/
  ShowControlBar(toolbar,status,FALSE);
}

/*====================================================================*/
void CMainFrame::ClearTimeStatusBarData() {
  /*====================================================================*/
  char *timeStepNbString = m_TimeStatusBar.GetTimeStepNbString();
  char *presentTimeString = m_TimeStatusBar.GetPresentTimeString();
  char *eigenModeIdString = m_TimeStatusBar.GetEigenModeIdString();
  /*----------------------*/
  /*  Clear data strings  */
  /*----------------------*/
  timeStepNbString[0] = 0; presentTimeString[0] = 0;
  eigenModeIdString[0] = 0;
  m_TimeStatusBar.SetEigenModeNumber(0);
  m_TimeStatusBar.SetTimeStatusBarText();
}

/*====================================================================*/
void CMainFrame::SetTimeStatusBarData
(int timeStepNb,   /* time step number */
 float presentTime /* present time     */ ) {
  /*====================================================================*/
  char *timeStepNbString = m_TimeStatusBar.GetTimeStepNbString();
  char *presentTimeString = m_TimeStatusBar.GetPresentTimeString();
  /*----------------------*/  
  /*  Set time step info  */
  /*----------------------*/  
  if (timeStepNb >= 0) {
    sprintf(timeStepNbString,"STEP %5d",timeStepNb);
    sprintf(presentTimeString,"TIME %8.3f",presentTime);
  }
  /*-------------------------------*/  
  /*  Set reference configuration  */
  /*-------------------------------*/  
  else {
    timeStepNbString[0] = 0;
    if (timeStepNb == -1) sprintf(presentTimeString,"REFERENCE");
    else presentTimeString[0] = 0;
  }
  m_TimeStatusBar.SetTimeStatusBarText();
}

/*====================================================================*/
void CMainFrame::SetTimeStatusBarModalData
(int eigenvalueNb, /* eigen mode number       */
 float eigr,       /* real part of eigenvalue */
 float eigi        /* imag part of eigenvalue */ ) {
  /*====================================================================*/
  char *eigenModeIdString = m_TimeStatusBar.GetEigenModeIdString();
  /*-------------------------------*/  
  /*  Construct eigen mode string  */
  /*-------------------------------*/
  if (eigenvalueNb) sprintf(eigenModeIdString,"Mode %3i. Freq: %8.3f i %8.3f",
			    eigenvalueNb,eigr,eigi);
  else eigenModeIdString[0] = 0;
  /*------------------*/  
  /*  Display string  */
  /*------------------*/
  m_TimeStatusBar.GetStatusBarCtrl().SetText(eigenModeIdString,3,0);
}

///////////////////////////////////////////////////////////////////////
// CMainFrame diagnostics

#ifdef _DEBUG
void CMainFrame::AssertValid() const
{
	CFrameWnd::AssertValid();
}

void CMainFrame::Dump(CDumpContext& dc) const
{
	CFrameWnd::Dump(dc);
}

#endif //_DEBUG

BEGIN_MESSAGE_MAP(CTimeStatusBar, CStatusBar)
  ON_WM_SIZE()
  END_MESSAGE_MAP()

/*====================================================================*/
afx_msg void CTimeStatusBar::OnSize
(UINT nType, int cx, int cy ) {
  /*====================================================================*/
  /*--------------------*/
  /*  Default resizing  */
  /*--------------------*/
  CStatusBar::OnSize(nType,cx,cy);
  /*-----------------------------------------------*/
  /* Menu status bar is sized to take whole width  */
  /* so need to change it back                     */
  /*-----------------------------------------------*/
  SetTimeStatusBarTextWidth();
  SetTimeStatusBarText();
}

/*====================================================================*/
int CTimeStatusBar::SetTimeStatusBarTextWidth() {
  /*====================================================================*/
  int width[4];
  if (GetStatusBarCtrl().GetParts(1,width)<1) return 0;
  width[0] -= 380;           width[1] = width[0] +  80;
  width[2] = width[1] + 100; width[3] = width[2] + 200;
  if (!GetStatusBarCtrl().SetParts(4,width)) return 0;
  return 1;
}

/*====================================================================*/
int CTimeStatusBar::SetTimeStatusBarText() {
  /*====================================================================*/
  if (!GetStatusBarCtrl().SetText(timeStepNbString,1,0)) return 0;
  if (!GetStatusBarCtrl().SetText(presentTimeString,2,0)) return 0;
  return 1;
}
