!***********************************************************
!*                                                         *
!* This module defines global constants needed for the     *
!* program but not necessary to be passed from outside     *
!* environment. These variables or their equivalent must   *
!* be defined in the outside environment, although it is   *
!* unnecessary to pass these variables externally          *
!* Some global functions also defined here, the equivalent *
!* must also be defined in the outside environmemt         *
!* Contains:                                               *
!*            FileOpen                                     *
!*            TitlePrint                                   *
!*            MemoryError                                  *
!*            IOError                                      *
!*            ConvertProblemControlParameters              *    
!*                                                         *
!* Copyrighted by Wenbin Yu                                *
!*                                                         *
!***********************************************************

MODULE GlobalDataFun


IMPLICIT NONE

!Global integer variables
!============================================================================
INTEGER:: allo_stat    ! flag to indicate status of allocating memory 
INTEGER:: in_stat      ! flag to indicate if the I/O process is successful

!==============Begin of Data defined in outside environment, but not necessary to pass to VABS
!==================================================================================================
!Global integer constants
!============================================================================
!--------------------------------------------------------------------------
! Define two global constants for short and long integer numbers  
!  
! INTEGER(SHT)::int_no_SHT   ! define a short integer number (-10^4-10^4)
! INTEGER(LNG)::int_no_LNG   ! define a long integer number  (-10^9-10^9)
!----------------------------------------------------------------------------
!INTEGER(2), PARAMETER::SHT=SELECTED_INT_KIND(4)
!INTEGER(2), PARAMETER::LNG=SELECTED_INT_KIND(9)

!--------------------------------------------------------------------------
! Define two global constants for single and double precision real numbers 
!  
! REAL(SGL)::real_no_SGL   ! define a single precision number
! REAL(DBL)::real_no_DBL   ! define a double precision number
! real_no_dbl=xxxxxx_DBL   ! initialize a double precision number
!----------------------------------------------------------------------------
!INTEGER, PARAMETER:: SGL=SELECTED_REAL_KIND(6)
INTEGER, PARAMETER:: DBL=SELECTED_REAL_KIND(15)


!Global real constants
!======================================================================
REAL(DBL),PARAMETER:: TOLERANCE = 1.0D-15     ! simulate a small number
REAL(DBL),PARAMETER:: PI        = 3.1415926535897932D0    
REAL(DBL),PARAMETER:: DEG_2_RAD = 1.7453292519943296D-2 ! the ratio between radians and degrees


!Global integer constants/variables, remain the same value 
!============================================================================
INTEGER, PARAMETER:: NDIM=2        ! dimension of the problem: cross-sectional analysis is 2D
INTEGER, PARAMETER:: MAX_NODE_ELEM=9    ! max number of nodes per element, VABS will handle up to 9-noded quads.
!INTEGER, PARAMETER:: LAY_CONST=10  ! layup constants including \theta_3 and 9 numbers for \theta_1.
INTEGER, PARAMETER:: NSTR_3D=6     ! number of strain or stress for 3D problem: 6.
INTEGER, PARAMETER:: NDOF_NODE=3   ! number of degrees of freedom per node
INTEGER, PARAMETER:: MAXDOF_EL=27  ! max d.o.f. per element:MAX_NODE_ELEM*NDOF_NODE
INTEGER, PARAMETER:: NE_1D=4       ! number of classical strains for 1D problem: 4.

!INTEGER           :: nsize         ! the size of the problem: nnode*NDOF_NODE

!==============End of Data defined in outside environment, but not necessary to pass to VABS
!==================================================================================================

CONTAINS
!=============================


!************************************************************
!*                                                          *
!*    To open an old or new file for reading or writing     *
!*															*
!************************************************************
FUNCTION 	FileOpen (file_unit,file_name,sta_type,rw_type,error,form)

LOGICAL                   ::FileOpen
INTEGER,INTENT(IN)        ::file_unit
CHARACTER(*),INTENT(IN)   ::file_name
CHARACTER(*),INTENT(IN)   ::sta_type
CHARACTER(*),INTENT(IN)   ::rw_type
CHARACTER(*),INTENT(OUT)::error

CHARACTER(*),OPTIONAL,INTENT(IN)   ::form 

error=''
FileOpen=.FALSE.

IF(PRESENT(form)) THEN
	OPEN (UNIT=file_unit, FORM=form,file=file_name,STATUS=sta_type,ACTION = rw_type,IOSTAT=in_stat)
ELSE
	OPEN (UNIT=file_unit, file=file_name,STATUS=sta_type,ACTION = rw_type,IOSTAT=in_stat)
ENDIF

IF (in_stat/=0) THEN
  IF(rw_type=='READ') error='Cannot open the file '//TRIM(file_name)//' for reading!'
  IF(rw_type=='WRITE')error='Cannot open the file '//TRIM(file_name)//' for writing!'
  IF(rw_type=='READWRITE')error='Cannot open the file '//TRIM(file_name)//' for reading & writing!'

ENDIF

IF(error/='')FileOpen=.TRUE.

END FUNCTION FileOpen
!***********************************************************


!************************************************************
!*                                                          *
!*        To print a title for a block of data              *
!*															*
!************************************************************
SUBROUTINE TitlePrint(file_unit, title)

INTEGER,INTENT(IN)        ::file_unit 
CHARACTER(*),INTENT(IN)   ::title

WRITE(file_unit,*) 
WRITE(file_unit,'(1x,100A)') title
WRITE(file_unit,*)'========================================================'
WRITE(file_unit,*) 

END SUBROUTINE TitlePrint
!***********************************************************


!************************************************************
!*                                                          *
!*        Check the error of memory allocation              *
!*															*
!************************************************************
FUNCTION  MemoryError(vari_name,error)

LOGICAL                 ::MemoryError
CHARACTER(*),INTENT(IN) ::vari_name         ! a character variable to hold variable name
CHARACTER(*),INTENT(OUT)::error

error=''
MemoryError=.FALSE.

IF(allo_stat/=0) THEN
	error='Memory error: allocate '//TRIM(vari_name)
    MemoryError=.TRUE.
ENDIF


END FUNCTION MemoryError
!***********************************************************


!************************************************************
!*                                                          *
!*        Check the error of I/O processing                 *
!*															*
!************************************************************
FUNCTION  IOError(message,error)

LOGICAL                 ::IOError
CHARACTER(*),INTENT(IN) ::message        ! a character variable to hold error message
CHARACTER(*),INTENT(OUT)::error

error=''
IOError=.FALSE.

IF(in_stat/=0) THEN 
    error='I/O error: '//TRIM(message)
    IOError=.TRUE.
ENDIF


END FUNCTION IOError
!***********************************************************




!*************************************************************
!*                                                           *
!*  Check whether there are repeated elements (nozero)       *
!*  in an array (integer)                                    *
!*														     *
!*************************************************************
FUNCTION  Repeated(n,array)

LOGICAL            ::Repeated
INTEGER,INTENT(IN) ::n,array(:)

INTEGER:: i,j,elem

Repeated=.FALSE.

DO i=1, n-1
   IF(array(i)/=0) THEN 
		elem=array(i)
   		DO j=i+1, n
			IF(elem==array(j)) THEN
				Repeated=.TRUE.
				RETURN
			ENDIF
		ENDDO
	ENDIF
ENDDO


END FUNCTION Repeated
!***********************************************************



END MODULE GlobalDataFun
!============================================================================
