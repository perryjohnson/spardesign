!***********************************************************
!*                    VABS (Version III)                   *
!*                                                         *
!*  --Variational Asymptotic Beam Sectional Analysis---    *
!*                                                         *
!*=========================================================*
!*                                                         *
!*               Author: Wenbin Yu                         *
!*                                                         *
!*          Mechanical and Aerospace Engineering           *
!*                                                         *
!*                Utah State University                    *
!*=========================================================*
!*                                                         * 
!*                 Version 3.0                             *
!*                                                         *
!*         Created on      : Jan     20, 2007              *
!*=========================================================*
!*                                                         *
!*                OBJECTIVE OF REVISION                    *
!*            =============================                *
!*                                                         * 
!* This new version is to finalize VABS and further        *
!* modulized VABS so that other cross-sectional analyses   *
!* can be easily added. Facilitate outside calls of VABS   *
!* from other programs                                     *
!*=========================================================*
!*                                                         * 
!*                 Version 3.1                             *
!*                                                         *
!*          Created on      : Sep. 3, 2008                 *
!*=========================================================*
!*                                                         *
!*                    Changes                              *
!*            =============================                *
!*                                                         * 
!* To modify VABS so that the standalone application can   *
!* be easily converted to a callable library. The user     *
!* needs to provide their own I/O handling for using VABS  *
!* as a callable library.                                  *
!*                                                         * 
!*=========================================================*
!*                                                         * 
!*                 Version 3.2                             *
!*                                                         *
!*          Released on      : Sep. 2009                   *
!*=========================================================*
!*                                                         *
!*                    Changes                              *
!*            =============================                *
!*                                                         * 
!* Thermoelastic modeling capabilities (3.2).              * 
!* Update Timoshenko transformation (3.2)                  *
!* Update License management (3.2.1)                       * 
!* Output the average of stresses/strains within each      *
!* element(3.2.2)                                          * 
!* Correct a bug with recovery (3.2.3)                     *
!* Add a linear option for recovery (3.2.4)                *
!* Output the warping functions in binary form to          * 
!* save time and increase accuracy (3.2.4.1)               *
!* Pass the arrays using explicit form for connecting with *
!* java interface. (3.2.4.2)                               *
!* change the order of statement to faciliate              *
!* interfacing with  Java and use gfortran compiled version*
!* for distribution. It is also much faster for some bigger* 
!* problems  (3.2.5)                                       *
!* add echo inside dll when the debug flag is on (3.2.5.1) *
!* fix a bug related with initialize error=''inside dlls   *
!*=========================================================*
!*                                                         * 
!*                 Version 3.3                             *
!*                                                         *
!*          Released on      : June 2010                   *
!*=========================================================*
!*                                                         *
!*                    Changes                              *
!*            =============================                *
!*                                                         * 
!* regroup some of the subroutines in until.f90 used by    *
!* recovery into preprocess.f90 (June 10)                  *
!* Introduce new input format by grouping all the layer    *
!* information together and avoid 9 numbers for theta1(3.3)*
!* (6/24/2010)                                             *
!* correct a bug with not passing density to recovery(3.3.1)*
!*=========================================================*
!*                                                         * 
!*                 Version 3.4                             *
!*                                                         *
!*          Released on      : Sept 2010                   *
!*=========================================================*
!*                                                         *
!*                    Changes                              *
!*            =============================                *
!*                                                         * 
!* correct the  \sqrt{g} problem                           *
!* use normal compile flags                                *  
!* simplify license mechanism using a simple subroutine    *
!*                                                         * 
!*=========================================================*
!*                 Version 3.5                             *
!*                                                         *
!*          Released on      : March 2011                  *
!*=========================================================*
!*                                                         *
!*                    Changes                              *
!*            =============================                *
!*                                                         * 
!* for oblique cross-sectional analysis, the inputs        *
!* are given in the oblique cross-sectional system         *
!* fix a bug with oblique parameters due to approximations *
!* used for double precision numbers (6/17/2011)           *
!* Use long names of input file, including spaces in the   *
!*    path and file names (7/19/2011)                      *
!***********************************************************

!***********************************************************




!=============================================================================
! Programming Style
!------------------------
!1. Global constants are in CAPITALS
! 
!2. Fortran statements and keywords are in CAPITALS
!
!3. Intrinsic function names are in CAPITALS
! 
!4. User defined functions, subroutines, and modules, capitalize
!   the first letter of each word only, such as MySubroutine
!
!5. All other variables, including global and local variables, are 
!   in lower cases with underscore to separate words, eg. my_variable
!   
!6. Never use stop in a subroutine or function, but return an error message
!
!7. If at all possible, do not modify an input for functions, which means 
!   all the arguments for functions should have INTENT(IN)
!
!8. Allow only necessary information of a module accessible to an outsite procedure
!   use USE ModuleName, ONLY: a list of names
!
!9. Use PRIVATE to protect any data which will not pass information to outsite procedures.
!
!10.Use meaningful names whenever possible
!
!11.Include a brief data dictionary in the header of any program unit
!
!12.Echo any variable input from the end user so that the user can check the data
!
!13.Always initialize all variables in a program before using them through declaration (preferred), read, assignment
!
!14.Always use IMPLICIT NONE.
!
!15.Always include a default case in the case construction
!
!16.Never modify the value of a DO loop index variable while inside the loop. Never use the value of the
!   index variable after the DO loop completes normaly. 
!
!17.Use ES to get conventional scientific description.
!
!18.Begin every format associated with a WRITE statement with the 1X descriptor. Hence all the output will begin from a new line
!
!19.Break large programs into procedures whenever practical
!
!20.Declare the intent of every dummy argument in every procedure.
!
!21.Goto is only used to direct to return to the calling program due to critical errors 
!=========================================================================================


PROGRAM VABS
USE CPUTime
USE VABSIO
 
IMPLICIT NONE ! Cancelling the naming convention of Fortran

INTERFACE
  SUBROUTINE ConstitutiveModeling (format_I,mat_type_layer,layup_angle,LAY_CONST,nlayer, &
                   Timoshenko_I, curved_I, oblique_I, trapeze_I, Vlasov_I, kb, beta, &
	               nnode, nelem, nmate, nsize, coord, element, layup, mat_type, material, orth, density,&
                   new_num,mass, xm2, xm3, mass_mc, I22, I33, mass_angle, Xg2, Xg3, V0, Aee, Aee_F, Xe2, &  
                   Xe3, V1, Aee_k, Aee_k_F, Xe2_k, Xe3_k, V1S, ST, ST_F, Sc1, Sc2, stiff_val,    &
                   stiff_val_F, Ag1, Bk1, Ck2, Dk3, thermal_I,cte, temperature,VT,NT,NT_F,error)
            USE GlobalDataFun
			!DEC$ ATTRIBUTES DLLIMPORT :: ConstitutiveModeling

			INTEGER,  INTENT(INOUT):: Timoshenko_I,curved_I,oblique_I,trapeze_I,Vlasov_I
			REAL(DBL),INTENT(INOUT):: kb(3),beta(3)
			INTEGER,  INTENT(IN)   :: nnode,nelem,nmate,nsize,LAY_CONST
			REAL(DBL),INTENT(INOUT):: coord(nnode,NDIM)
			INTEGER,  INTENT(INOUT):: element(nelem,MAX_NODE_ELEM)  
			REAL(DBL),INTENT(INOUT):: layup(nelem,LAY_CONST) 
			INTEGER,  INTENT(IN)   :: mat_type(nelem)
			REAL(DBL),INTENT(IN)   :: material(nmate,21)
			INTEGER,  INTENT(IN)   :: orth(nmate)
		    REAL(DBL),INTENT(IN)   :: density(nmate)
  
			INTEGER, INTENT(OUT)   :: new_num(nnode)
			REAL(DBL),INTENT(OUT)  :: mass(6,6),xm2, xm3,mass_mc(6,6),I22, I33, mass_angle,Xg2,Xg3 ! mass properties and centroid
			REAL(DBL),INTENT(OUT)  :: V0(nsize,NE_1D),Aee(NE_1D,NE_1D),Aee_F(NE_1D,NE_1D),Xe2,Xe3              !Output for classical modeling
			REAL(DBL),INTENT(OUT)  :: V1(nsize,NE_1D),Aee_k(NE_1D,NE_1D),Aee_k_F(NE_1D,NE_1D),Xe2_k,Xe3_k      !Output for curved/twisted modeling
			REAL(DBL),INTENT(OUT)  :: V1S(nsize,NE_1D),ST(6,6),ST_F(6,6),Sc1,Sc2  !Output for Timoshenko modeling
			REAL(DBL),INTENT(OUT)  :: stiff_val(5,5),stiff_val_F(5,5)     !Output for Vlasov modeling
			REAL(DBL),INTENT(OUT)  :: Ag1(4,4),Bk1(4,4),Ck2(4,4),Dk3(4,4) !Outputs for Trapeze effect

! Variables for thermoelastic analysis
!---------------------------------------------------------------
		    INTEGER,  INTENT(INOUT):: thermal_I
			REAL(DBL),INTENT(IN)   :: cte(nmate,6)
			REAL(DBL),INTENT(INOUT):: temperature(nnode)
			REAL(DBL),INTENT(OUT)  :: VT(nsize),NT(4),NT_F(4)
!---------------------------------------------------------------

			CHARACTER(300),INTENT(OUT)::error
! Variables needed for new vabs input format
!------------------------------------------------
			INTEGER,INTENT(IN):: format_I,nlayer
			INTEGER,INTENT(IN):: mat_type_layer(nlayer)
			REAL(DBL),INTENT(INOUT)::layup_angle(nlayer)
!------------------------------------------------------------


  END SUBROUTINE ConstitutiveModeling
END INTERFACE
 

INTERFACE
  SUBROUTINE Recovery (format_I,mat_type_layer,layup_angle,LAY_CONST,nlayer,&
                   recover_I,Timoshenko_I, curved_I, oblique_I, Vlasov_I, kb, beta,              &
                   nnode, nelem, nmate, nsize,coord, element, layup, mat_type,  material, orth,density,&
                   new_num,disp_1D, dir_cos_1D, strain_CL, strain_CL_1, strain_CL_2,   &
                   force_1D, load_1D, load1_1D, load2_1D, V0, Aee_F, V1, V1S, ST_F,      &
               	   disp_3D_F, k_F, nd_F, ss_F, ss_nd_F,ss_elem,thermal_I,cte,temperature,VT,NT_F,error)
             
			 USE GlobalDataFun
			!DEC$ ATTRIBUTES DLLIMPORT :: Recovery

			INTEGER,  INTENT(INOUT):: recover_I, Timoshenko_I, curved_I, oblique_I, Vlasov_I
			REAL(DBL),INTENT(INOUT):: kb(3),beta(3)
			INTEGER,  INTENT(IN)   :: nnode,nelem,nmate, nsize,LAY_CONST
		    REAL(DBL),INTENT(INOUT):: coord(nnode,NDIM)	
			INTEGER,  INTENT(INOUT):: element(nelem,MAX_NODE_ELEM)  
			REAL(DBL),INTENT(INOUT):: layup(nelem,LAY_CONST)
    		INTEGER,  INTENT(IN)   :: mat_type(nelem)
			REAL(DBL),INTENT(IN)   :: material(nmate,21),density(nmate)
			INTEGER,  INTENT(IN)   :: orth(nmate)
			INTEGER, INTENT(OUT)   :: new_num(nnode)
			REAL(DBL),INTENT(IN)   :: disp_1D(3)
			REAL(DBL),INTENT(INOUT):: dir_cos_1D(3,3),strain_CL(4),strain_CL_1(4), strain_CL_2(4)
			REAL(DBL),INTENT(IN)   :: force_1D(6),load_1D(6),load1_1D(6), load2_1D(6)
			REAL(DBL),INTENT(IN)   :: V0(nsize,NE_1D),Aee_F(NE_1D,NE_1D),V1(nsize,NE_1D),V1S(nsize,NE_1D),ST_F(6,6)
			REAL(DBL),INTENT(OUT)  :: disp_3D_F(nnode,5)
			INTEGER,INTENT(OUT)    :: k_F,nd_F
			REAL(DBL),INTENT(OUT)  :: ss_F(nelem*MAX_NODE_ELEM,26),ss_nd_F(nelem*MAX_NODE_ELEM,26),ss_elem(nelem,24)
			
			! Variables for thermoelastic analysis
!---------------------------------------------------------------
		    INTEGER,  INTENT(INOUT) :: thermal_I
			REAL(DBL),INTENT(IN)    :: cte(nmate,6)
			REAL(DBL),INTENT(INOUT) :: temperature(nnode)
			REAL(DBL),INTENT(IN)    :: VT(nsize),NT_F(4)
!---------------------------------------------------------------

			CHARACTER(300),INTENT(OUT)::error
! Variables needed for new vabs input format
!------------------------------------------------
			INTEGER,INTENT(IN):: format_I,nlayer
			INTEGER,INTENT(IN):: mat_type_layer(nlayer)
			REAL(DBL),INTENT(INOUT)::layup_angle(nlayer)
!------------------------------------------------------------

  END SUBROUTINE Recovery
END INTERFACE
 
REAL:: 	compute_time  ! time used for analysis


CALL Input ! Read inputs for the cross-sectional analysis: in VABSIO
IF(error/='')	 GOTO 9999
WRITE(*,*) 
WRITE(*,*) 'Finished reading inputs for the cross-sectional analysis.'
CALL TIC


!====================================Begin recovery     
IF(recover_I/=0) THEN 

    CALL RecoveryInput ! Read inputs for recovery: in VABSIO
    IF(error/='')	 GOTO 9999
	CALL TIC

	WRITE(*,*) 
    WRITE(*,*) 'Finished reading data from constitutive modeling needed for recovery.'
   
    CALL Recovery (format_I,mat_type_layer,layup_angle,LAY_CONST,nlayer, &
	               recover_I,Timoshenko_I, curved_I, oblique_I, Vlasov_I, kb, beta,              &
                   nnode, nelem, nmate,nsize, coord, element, layup, mat_type,  material, orth,density,&
                   new_num,disp_1D, dir_cos_1D, strain_CL, strain_CL_1, strain_CL_2,  &
                   force_1D, load_1D, load1_1D, load2_1D, V0, Aee_F, V1, V1S, ST_F,      &
               	   disp_3D_F, k_F, nd_F, ss_F, ss_nd_F,ss_elem,thermal_I,cte,temperature,VT,NT_F,error)

	IF(error/='')	 GOTO 9999
  	WRITE(*,*)
	WRITE(*,*)'Finished recovery'

	compute_time=TOC()
	
	CALL RecoveryOutput ! Output recovery results: in VABSIO
    IF(error/='')	 GOTO 9999
  	WRITE(*,*)
	WRITE(*,*)'Finished outputing recovery results'
	
    !====================================End recovery     

ELSE  

    !====================================Begin constitutive modeling    
	CALL ConstitutiveModeling (format_I,mat_type_layer,layup_angle,LAY_CONST,nlayer,Timoshenko_I, curved_I, &
	               oblique_I, trapeze_I, Vlasov_I, kb, beta, &
	               nnode, nelem, nmate, nsize,coord, element, layup, mat_type, material, orth, density,&
                   new_num,mass, xm2, xm3, mass_mc, I22, I33, mass_angle, Xg2, Xg3, V0, Aee, Aee_F, Xe2, &  
                   Xe3, V1, Aee_k, Aee_k_F, Xe2_k, Xe3_k, V1S, ST, ST_F, Sc1, Sc2, stiff_val,    &
                   stiff_val_F, Ag1, Bk1, Ck2, Dk3, thermal_I,cte, temperature,VT,NT,NT_F,error)


    IF(error/='')	 GOTO 9999
    WRITE(*,*)
	WRITE(*,*)'Finished constitutive modeling' 

   	compute_time=TOC()

   	CALL Output  ! Output constitutive modeling results: in VABSIO
    IF(error/='')	 GOTO 9999
	WRITE(*,*)
	WRITE(*,*)'Finished outputing constitutive modeling results' 

    !====================================End constitutive modeling

ENDIF


WRITE(*,*)
WRITE(*,*)'VABS finished successfully'
WRITE(*,*)
WRITE(*,*)'VABS Runs for  ', compute_time,' Seconds.'

9999 IF(error/='') WRITE(*,*) error 
     CALL WriteError ! Write error to the echo file: in VABSIO
	 

END 
!**************************************************************