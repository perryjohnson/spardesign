!******************************************************
!*                                                    *
!* This module handles I/O of the program including   *
!* definition of inputs/outputs, reading inputs from  *
!* a data file, echo inputs, and write outputs        *
!* to data files. To interface VABS with outside      *
!* environment, one needs to provide such             *
!* capability from the outside environment.           *
!*                                                    *
!* Copyrighted by Wenbin Yu                           *
!******************************************************
MODULE VABSIO

USE GlobalDataFun

IMPLICIT NONE



!============================Begin of Private Data: only used in this module

! files needed/generated for constitutive modeling
!======================================================
INTEGER,PARAMETER        :: CHAR_LEN=256
INTEGER,PARAMETER,PRIVATE:: IN  =10     ! input file: inp_name
CHARACTER(CHAR_LEN)      :: inp_name    ! it was made public in VABS3.6 for passing it to dlls for output new numbering and warping functions

INTEGER,PARAMETER,PRIVATE:: EIN =20     ! file for echoing the inputs: inp_name.ech, EIN is needed for the main program
CHARACTER(CHAR_LEN+3),PRIVATE    :: ech_name 

INTEGER,PARAMETER,PRIVATE:: OUT =40     ! file for output: inp_name.K
CHARACTER(CHAR_LEN+1),PRIVATE    :: out_name 

! files needed/generated for recovery
!======================================================
INTEGER,PARAMETER,PRIVATE:: uout=101              !file storing nodal displacements in global coordinate system           
CHARACTER(CHAR_LEN+1),PRIVATE    :: u_name               

INTEGER,PARAMETER,PRIVATE:: eout=110, sout=120    ! files storing Gaussian strain/stress values in global coordinate system
CHARACTER(CHAR_LEN+1),PRIVATE    :: e_name,s_name         

INTEGER,PARAMETER,PRIVATE:: emout=130, smout=140  ! files storing Gaussian strain/stress values in material system
CHARACTER(CHAR_LEN+2),PRIVATE    :: em_name,sm_name      

INTEGER,PARAMETER,PRIVATE:: enout=150, snout=160  ! files storing nodal strain/stress values in global coordinate system
CHARACTER(CHAR_LEN+2),PRIVATE    :: en_name,sn_name      


INTEGER,PARAMETER,PRIVATE:: emnout=170, smnout=180 ! files storing nodal strain/stress values in material system
CHARACTER(CHAR_LEN+3),PRIVATE    :: emn_name,smn_name      

INTEGER,PARAMETER,PRIVATE:: elemout=190 ! files storing average stress/strain values at Gaussian points within one element
CHARACTER(CHAR_LEN+3),PRIVATE    :: elem_name      

!=============================End of Private Data



!=================================Begin of Input needed for the program

! Global logical variables
!--------------------------------------------------------------------------------
INTEGER:: Timoshenko_I   ! if it is 1, VABS will carry out a Timoshenko modeling
INTEGER:: curved_I       ! if it is 1, the beam is initially curved or twisted
INTEGER:: oblique_I      ! if it is 1, the beam has an oblique referencecross section
INTEGER:: trapeze_I      ! if it is 1, VABS will capture the trapeze effect
INTEGER:: Vlasov_I       ! if it is 1, VABS will carry out a Vlasov modeling
INTEGER:: recover_I      ! if it is 1, the program will perform recovery



!Global integer variables
!--------------------------------------------------------------------------------
INTEGER            ::nnode         ! number of nodes
INTEGER            ::nelem         ! number of elements
INTEGER            ::nmate         ! number of materials
INTEGER,ALLOCATABLE::element(:,:)  ! elemental connectivity: element(nelem,MAX_NODE_ELEM) 
INTEGER,ALLOCATABLE::mat_type(:)   ! material type for each element: mat_type(nelem)
INTEGER,ALLOCATABLE::orth(:)       ! indicate whether a material is isotropic (0), orthotropic (1), or anisotropic (2): orth(nmate)  


! Global real variables
!--------------------------------------------------------------------------------
REAL(DBL)            :: kb(3)    ! the initial curvatures/twist
REAL(DBL)            :: beta(3)  ! the three oblique parameters 
REAL(DBL),ALLOCATABLE:: coord(:,:)    ! nodal coordinates: coord(nnode,NDIM)
REAL(DBL),ALLOCATABLE:: layup(:,:)    ! layup parameters:  layup(nelem,LAY_CONST) 
REAL(DBL),ALLOCATABLE:: material(:,:) ! constants for each material: material(nmate,21)
REAL(DBL),ALLOCATABLE:: density(:)    ! material density: density(nmate)


! Input data needed for recovery
!--------------------------------------------------------------------------------
REAL(DBL)::disp_1D(3)        ! 1D global displacements from the beam analysis
REAL(DBL)::dir_cos_1D(3,3)   ! 1D global rotation matrix for recovery
REAL(DBL)::strain_CL(4) ! Classical strain measures
REAL(DBL)::strain_CL_1(4), strain_CL_2(4)  ! First and second derivatives of classical strain measures
REAL(DBL)::force_1D(6)       ! 1D stress resultants
REAL(DBL)::load_1D(6)        ! Distributed loads (including inertial loads)
REAL(DBL)::load1_1D(6), load2_1D(6) ! First and second derivatives of distributed loads (including inertial loads)

!======================End of inputs needed for VABS



!=======================================Begin of Output variables needed for the program

!Global real variables
!============================================================================
REAL(DBL):: mass(6,6)          ! The mass matrix 
REAL(DBL):: xm2, xm3           ! The mass center
REAL(DBL):: mass_mc(6,6)       ! The mass matrix at the mass center
REAL(DBL):: I22, I33           ! Mass moments of inertia along x2 and x3
REAL(DBL):: mass_angle         ! The angle of principal inertial axes

REAL(DBL):: Xg2,Xg3            ! Geometric center 

REAL(DBL):: Aee(NE_1D,NE_1D)   ! Classical stiffness matrix
REAL(DBL):: Aee_F(NE_1D,NE_1D) ! Classical flexibility matrix
REAL(DBL):: Xe2,Xe3            ! Tension center
REAL(DBL):: Aee_k(NE_1D,NE_1D) ! Classical stiffness matrix of an initially curved/twisted beam
REAL(DBL):: Aee_k_F(NE_1D,NE_1D)! Classical flexibility matrix of an initially curved/twisted beam
REAL(DBL):: Xe2_k,Xe3_k        ! Tension center of an initially curved/twisted beam

REAL(DBL):: ST(6,6)            ! The six by six Timoshenko stiffness matrix
REAL(DBL):: ST_F(6,6)          ! The six by six Timoshenko flexibility matrix
REAL(DBL):: Sc1,Sc2            ! Shear center
REAL(DBL):: stiff_val(5,5)     ! The 5x5 Vlasov stiffness matrix
REAL(DBL):: stiff_val_F(5,5)   ! The 5x5 Vlasov flexibility matrix

REAL(DBL):: Ag1(4,4)           ! The matrices for Trapeze effects.
REAL(DBL):: Bk1(4,4) 
REAL(DBL):: Ck2(4,4)
REAL(DBL):: Dk3(4,4)

!Global character variables
!============================================================================
CHARACTER(300)::error         ! a character variable to hold the error message


! Output data needed for recovery
!--------------------------------------------------------------------------------
REAL(DBL),ALLOCATABLE::disp_3D_F(:,:), ss_F(:,:),ss_nd_F(:,:),ss_elem(:,:) ! 3D fields 
INTEGER:: k_F, nd_F  ! the total number of Guassian points and nodes we have recovered 3D fields for.

! Variables for thermoealstic modeling
!-----------------------------------------------
INTEGER:: thermal_I      ! if it is 3, VABS will perform the one-way coupled thermoelastic c/s analsyis; 
                         ! if it is 0, VABS will not perform any thermal-related analysis
REAL(DBL),ALLOCATABLE:: cte(:,:) ! CTE constants for each material: cte(nmate,6)
REAL(DBL),ALLOCATABLE:: temperature(:) ! nodal temperature: temperature(nnode)
REAL(DBL)            :: NT(4)    ! 1D nonmechanical stress resultants
REAL(DBL)            :: NT_F(4)    ! 1D thermal strains

! Variables needed for new vabs input format
!------------------------------------------------
INTEGER:: format_I  ! format_I ==1, new format, otherwise old format
INTEGER:: nlayer    ! number of layers
INTEGER:: LAY_CONST ! layup constants: 10 for old format including \theta_3 and 9 number for \theta1; 1 for new format for 1 number for \theta1
INTEGER,ALLOCATABLE:: mat_type_layer(:) ! material type for each layer
REAL(DBL),ALLOCATABLE::layup_angle(:)   ! layup orientation for each layer
!------------------------------------------------------------


CONTAINS
!=============================


!*************************************************************
!*                                                           *
!* To read and echo the cross-sectional finite element model * 
!*															 *
!*************************************************************
SUBROUTINE Input

INTEGER:: i,j
INTEGER::node_no      ! temporary node number
INTEGER::elem_no      ! temporary element number
CHARACTER(20)::tmp_char         ! a temporary character variable to write integer numbers.
INTEGER::mat_id                 ! temporary number for material type
INTEGER::mate_const     ! 2 for isotropic; 9 for orthotropic; 21 for general anisotropic 
INTEGER::cte_const   ! CTE constants 1 for isotropic; 3 for orthotropic; 6 for general anisotropic 

INTEGER,ALLOCATABLE::node_no_arr(:),elem_no_arr(:)


CALL GETARG(1,inp_name)
IF(TRIM(inp_name)=='') THEN
 error='Please provide an input file name, executing as VABSIII input_file_name'
 RETURN
ENDIF
IF(FileOpen(IN, inp_name, 'OLD', 'READ',error))	 RETURN 

! Create a file name for echoing the input data
!--------------------------------------------------
ech_name=TRIM(inp_name) // ".ech" 
IF(FileOpen(EIN,  ech_name,'REPLACE','WRITE',error))	 GOTO 9999

! Input and echo format control parameters.
!---------------------------------------------------------
READ(IN,*,IOSTAT=in_stat) format_I,nlayer  
IF(IOError('read format parameter and # of layers',error)) GOTO 9999

CALL TitlePrint(EIN, 'Format Control Parameter')
IF(format_I==1)THEN
	WRITE(EIN,*) "New Input Format is using"
	WRITE(EIN,*) "There are", nlayer, "layers"
	LAY_CONST=1
	IF(nlayer<1) THEN
	   error='nlayer cannot be smaller than 1'
	   GOTO 9999
	ENDIF
ELSE
	WRITE(EIN,*) "Old Input Format is using"   
    LAY_CONST=10
ENDIF


! Input and echo problem control parameters.
!---------------------------------------------------------
READ(IN,*,IOSTAT=in_stat) Timoshenko_I, recover_I, thermal_I  
IF(IOError('read problem conontrol parameters',error)) GOTO 9999


CALL TitlePrint(EIN, 'Control Parameters')
WRITE(EIN,*) "Timoshenko  = ", Timoshenko_i
WRITE(EIN,*) "Recovery    = ", recover_i
WRITE(EIN,*) "Thermal Analysis= ", thermal_I

READ(IN,*,IOSTAT=in_stat) curved_I, oblique_I, trapeze_I, Vlasov_I 
IF(IOError('read problem conontrol parameters',error)) GOTO 9999

WRITE(EIN,*) "Curved      = ", curved_I   
WRITE(EIN,*) "Oblique     = ", oblique_I 
WRITE(EIN,*) "Trapeze     = ", trapeze_I   
WRITE(EIN,*) "Vlasov      = ", Vlasov_I   


! Input and echo initial twist/curvatures
!----------------------------------------------------------------
kb=(/0.d0,0.d0,0.d0/) ! initialize
IF(curved_I==1) THEN 
	READ(IN,*,IOSTAT=in_stat) kb
	IF(IOError('read initial curvatures/twist',error)) GOTO 9999
    
	CALL TitlePrint(EIN, 'Initial Curvatures/Twist')
	WRITE(EIN,*) "k1= ", kb(1)
	WRITE(EIN,*) "k2= ", kb(2)
	WRITE(EIN,*) "k3= ", kb(3)
		
ENDIF


! Input and echo obliqueness
!----------------------------------------------------------------
beta=(/1.d0,0.d0,0.d0/)
IF(oblique_I==1) THEN 
 
    READ(in,*,IOSTAT=in_stat)(beta(i),i = 1, 2)
	IF(IOError('read oblique parameters',error)) GOTO 9999
	 
    CALL TitlePrint(EIN, 'Oblique Parameters')
   	WRITE(EIN,*)'beta1=',beta(1)
    WRITE(EIN,*)'beta2=',beta(2)
   
ENDIF


! Input and echo mesh control parameters
!----------------------------------------------------------------
READ(IN,*,IOSTAT=in_stat) nnode, nelem, nmate
IF(IOError('read mesh conontrol parameters',error)) GOTO 9999

CALL TitlePrint(EIN, 'Mesh control parameters')
WRITE(EIN,*) "Nodes         = ", nnode
WRITE(EIN,*) "Elements      = ", nelem
WRITE(EIN,*) "Material Types= ", nmate	



! Input and echo nodal coordinates
!----------------------------------------------------------------
ALLOCATE(coord(nnode,NDIM),STAT=allo_stat)
IF(MemoryError('coord',error)) GOTO 9999
coord=0.0D0

ALLOCATE(node_no_arr(nnode),STAT=allo_stat)
IF(MemoryError('node_no_arr',error)) GOTO 9999
node_no_arr=0

DO i=1,nnode

   READ(IN,*,IOSTAT=in_stat)node_no,coord(node_no,1:NDIM)
   IF(IOError('read nodal coordinates',error)) GOTO 9999
  
   node_no_arr(i)=node_no

   IF(node_no>nnode) THEN
      WRITE(tmp_char, *) node_no
      error='I/O error: node # '//TRIM(tmp_char)//' is greater than the total number of nodes'
      GOTO 9999
   ENDIF
 
ENDDO   


!Test whether all the nodes (1 to nnode) are in the nodal coordinate input
!-------------------------------------------------------------
DO i=1,nnode

   IF(ALL(i/=node_no_arr))THEN  ! If i does not belong to any of node_no_arr
      WRITE(tmp_char, *) i
      error='I/O error: node # '//TRIM(tmp_char)//' does not exist in the nodal coordinate inputs'
      GOTO 9999
   ENDIF

ENDDO


CALL TitlePrint(EIN, 'Nodal Coordinates')
WRITE(EIN,'(1X,i8,2ES20.10)') (i,coord(i,:),i=1,nnode)


! Input and echo elemental connectivity
!----------------------------------------------------------------
ALLOCATE(element(nelem,MAX_NODE_ELEM),STAT=allo_stat)
IF(MemoryError('element',error)) GOTO 9999
element=0


ALLOCATE(elem_no_arr(nelem),STAT=allo_stat)
IF(MemoryError('elem_no_arr',error)) GOTO 9999
elem_no_arr=0


DO i=1,nelem 
   READ(IN,*,IOSTAT=in_stat)elem_no, element(elem_no,1:MAX_NODE_ELEM)
   IF(IOError('read elemental connectivity',error)) GOTO 9999

   elem_no_arr(i)=elem_no

   IF(Repeated(MAX_NODE_ELEM,element(elem_no,:))) THEN  
      WRITE(tmp_char, *) elem_no
   	  error='You have repeated nodes for element'//TRIM(tmp_char)
	  GOTO 9999
   ENDIF
   
   IF(elem_no>nelem) THEN
      WRITE(tmp_char, *) elem_no
      error='I/O error: element # '//TRIM(tmp_char)//' is greater than the total number of elements'
   	  GOTO 9999
   ENDIF
 
ENDDO   


!Test whether all the elements (1 to nelem) are in the elemental connectivity input
!-------------------------------------------------------------

DO i=1,nelem

   IF(ALL(i/=elem_no_arr))THEN
      WRITE(tmp_char, *) i
      error='I/O error: element # '//TRIM(tmp_char)//' does not exist in the elemental connectivity inputs'
      GOTO 9999
   ENDIF

ENDDO

CALL TitlePrint(EIN, 'Element Definition (Nodes)')
CALL TitlePrint(EIN, '   Elem#.  N1    N2    N3     N4   N5    N6    N7    N8    N9 ')
WRITE(EIN,'(1X,i8,9i8)') (i,element(i,:),i=1,nelem)



! Input and echo elemental layup parameters
!----------------------------------------------------------------
ALLOCATE(layup(nelem,LAY_CONST),STAT=allo_stat)
IF(MemoryError('layup',error)) GOTO 9999
layup=0.0D0

ALLOCATE(mat_type(nelem),STAT=allo_stat)
IF(MemoryError('mat_type',error)) GOTO 9999
mat_type=0

IF(format_I==1) THEN
	DO i=1,nelem
		READ(IN,*,IOSTAT=in_stat) elem_no,mat_type(elem_no),layup(elem_no,1:LAY_CONST)
		IF(IOError('read layer type and \theta_1 for each element',error)) GOTO 9999
   
		IF(mat_type(elem_no)>nlayer) THEN
			WRITE(tmp_char, *) elem_no
			error='I/O error: layer # for element'//TRIM(tmp_char)//' is greater than the total number of layers'
			GOTO 9999
		ENDIF

		IF(mat_type(elem_no)<=0)THEN
			WRITE(tmp_char, *) elem_no
			error='Data error: layer # cannot be zero or negative: element'//TRIM(tmp_char)
			GOTO 9999
		ENDIF
	ENDDO       
   

	CALL TitlePrint(EIN, 'Elemental Layup Definitions')
	CALL TitlePrint(EIN, 'Elem#    Layer#   theta1 ')
	WRITE(EIN,'(1x,i8,i8,ES20.10)') (i,mat_type(i),layup(i,:),i=1,nelem)

ELSE

	DO i=1,nelem
		READ(IN,*,IOSTAT=in_stat) elem_no,mat_type(elem_no),layup(elem_no,1:LAY_CONST)
		IF(IOError('read material type and layup for elements',error)) GOTO 9999
   
		IF(mat_type(elem_no)>nmate) THEN
			WRITE(tmp_char, *) elem_no
			error='I/O error: material # for element'//TRIM(tmp_char)//' is greater than the total number of material types'
			GOTO 9999
		ENDIF

		IF(mat_type(elem_no)<=0)THEN
			WRITE(tmp_char, *) elem_no
			error='Data error: material number cannot be zero or negative: element'//TRIM(tmp_char)
			GOTO 9999
		ENDIF
	ENDDO       
   

	CALL TitlePrint(EIN, 'Elemental Layup Definitions')
	CALL TitlePrint(EIN, 'Elem#    Mat#   Parameter1    Parameter2 ')
	WRITE(EIN,'(1x,i8,i8,10ES20.10)') (i,mat_type(i),layup(i,:),i=1,nelem)

ENDIF

IF(format_I==1) THEN
! Input and echo layup information
!----------------------------------------------------------------
ALLOCATE(layup_angle(nlayer),STAT=allo_stat)
IF(MemoryError('layup_angle',error)) GOTO 9999
layup_angle=0.0D0

ALLOCATE(mat_type_layer(nlayer),STAT=allo_stat)
IF(MemoryError('mat_type_layer',error)) GOTO 9999
mat_type_layer=0

	DO i=1,nlayer
		READ(IN,*,IOSTAT=in_stat) elem_no,mat_type_layer(elem_no),layup_angle(elem_no) ! note here elem_no is layer_no
		IF(IOError('read material type and theta3 for each layer',error)) GOTO 9999
   
		IF(mat_type_layer(elem_no)>nmate) THEN
			WRITE(tmp_char, *) elem_no
			error='I/O error: material # for layer'//TRIM(tmp_char)//' is greater than the total number of materials'
			GOTO 9999
		ENDIF

		IF(mat_type_layer(elem_no)<=0)THEN
			WRITE(tmp_char, *) elem_no
			error='Data error: material # cannot be zero or negative: layer'//TRIM(tmp_char)
			GOTO 9999
		ENDIF
	ENDDO       
   
	CALL TitlePrint(EIN, 'Layup Definitions')
	CALL TitlePrint(EIN, 'Layer#  Material# theta1 ')
	WRITE(EIN,'(1x,i8,i8,ES20.10)') (i,mat_type_layer(i),layup_angle(i),i=1,nlayer)
ENDIF


! Input and echo material constants for each material type
!----------------------------------------------------------------
ALLOCATE(orth(nmate),STAT=allo_stat)
IF(MemoryError('orth',error)) GOTO 9999
orth=0

ALLOCATE(material(nmate,21),STAT=allo_stat)
IF(MemoryError('material',error)) GOTO 9999
material=0.0D0

ALLOCATE(density(nmate),STAT=allo_stat)
IF(MemoryError('density',error)) GOTO 9999
density=0.0D0

IF(thermal_I==3)THEN 
	ALLOCATE(cte(nmate,6),STAT=allo_stat)
	IF(MemoryError('CTE',error)) GOTO 9999
	cte=0.0D0
ENDIF


DO i=1,nmate
	
	READ(IN,*,IOSTAT=in_stat)mat_id, orth(mat_id)  ! read in material type and characteristics
	IF(IOError('read material type and characteristics',error)) GOTO 9999
	
	IF(mat_id>nmate) THEN
        WRITE(tmp_char, *) i
	    error='I/O error: material # for material'//TRIM(tmp_char)//' is greater than the total number of material types'
		GOTO 9999
	ENDIF
    
	WRITE(EIN,*) 
    WRITE(EIN,*) '       Properties for material No.', mat_id
			
	SELECT CASE (orth(mat_id))
	       CASE(0)      ! isotropic material 
			 mate_const=2
             
			 IF(thermal_I==3) cte_const=1
			 
			 WRITE(EIN,*) 'Isotropic'	    
		     
			   
		   CASE(1)  !orthotropic material
          	 mate_const=9

			 IF(thermal_I==3)  cte_const=3
			 
			 WRITE(EIN,*) 'Orthotropic'

		 
           CASE(2) ! general anisotropic material
		     mate_const=21

			 IF(thermal_I==3) cte_const=6
    	     
			 WRITE(EIN,*) 'Anisotropic'
	     
	       CASE DEFAULT 
		     error="For material characteristics, please use 0 for isotropic, 1 for orthotropic, and 2 for anisotropic."
			 GOTO 9999
		 !---------------------------------------------------------------------------   
    END SELECT
    IF(material(mat_id,1)==0.0D0)THEN
		READ(IN,*,IOSTAT=in_stat)material(mat_id,1:mate_const)
		IF(IOError('read material constants',error)) GOTO 9999
	
		READ(IN,*,IOSTAT=in_stat)density(mat_id)
		IF(IOError('read material density',error)) GOTO 9999
		
		WRITE(EIN,'(1X,3ES20.10)')material(mat_id,1:mate_const)
		WRITE(EIN,'(1X,1ES20.10)')density(mat_id)
	

		IF (thermal_I==3)THEN
			READ(IN,*,IOSTAT=in_stat)cte(mat_id, 1:cte_const)
			IF(IOError('read coefficients of thermal expansion',error)) GOTO 9999
			WRITE(EIN,'(1X,1ES20.10)')cte(mat_id,1:cte_const)
		ENDIF
	 ELSE
       WRITE(error,*)"The properties for material",mat_id," have already been assigned!"
	   GOTO 9999
	 ENDIF
ENDDO

! Input and echo nodal temperature
!----------------------------------------------------------------
IF(thermal_I==3) THEN
	ALLOCATE(temperature(nnode),STAT=allo_stat)
    IF(MemoryError('temperature',error)) GOTO 9999
	temperature=0.0D0

	DO i=1,nnode

		READ(IN,*,IOSTAT=in_stat)node_no,temperature(node_no)
		IF(IOError('read nodal temperature',error)) GOTO 9999
   
		IF(node_no>nnode) THEN
			WRITE(tmp_char, *) node_no
			error='I/O error: node # '//TRIM(tmp_char)//' is greater than the total number of nodes'
			GOTO 9999
		ENDIF
 
	ENDDO   

	CALL TitlePrint(EIN, 'Nodal Temperature')
	WRITE(EIN,'(1X,i8,1ES20.10)') (i,temperature(i),i=1,nnode)
ENDIF 

!
! Read the global behavior which is also provided in inp_name
!----------------------------------------------------------------
IF(recover_I/=0) THEN
	
	READ(in,*,IOSTAT=in_stat) disp_1D  ! read 1D beam displacements
	IF(IOError('read global beam displacements',error)) GOTO 9999
	
	READ(in,*,IOSTAT=in_stat) (dir_cos_1D(i,:),i=1,3)  ! read the 1D global rotation matrix
    IF(IOError('read global rotation matrix',error)) GOTO 9999
	

	CALL TitlePrint(EIN, '1D Displacement and Direction Cosine Matrix')
	WRITE(EIN,'(1x,3ES20.10)') disp_1D
	WRITE(EIN,'(1x,3ES20.10)') (dir_cos_1D(i,:),i=1,3)
    
	strain_CL=0.0D0;strain_CL_1=0.D0; strain_CL_2=0.D0

	IF(Vlasov_I==1) THEN ! Read 1D strain measures and their derivatives for recovery based on Vlasov model 
		READ(in,*,IOSTAT=in_stat) strain_CL, strain_CL_1(2), strain_CL_2(2)
        IF(IOError('read strain measures for recovery based on Vlasov model',error)) GOTO 9999
		
		CALL TitlePrint(EIN, '1D Strains and Derivatives of Vlasov Model')
		WRITE(EIN,'(1x,4ES20.10)') strain_CL
		WRITE(EIN,'(1x,4ES20.10)') strain_CL_1
		WRITE(EIN,'(1x,4ES20.10)') strain_CL_2

	ELSE

		READ(in,*,IOSTAT=in_stat) force_1D(1),force_1D(4),force_1D(5),force_1D(6) !Read stress resultants for classical model
		IF(IOError('read stress resultants F1,M1,M2,M3',error)) GOTO 9999
	
		CALL TitlePrint(EIN, '1D Stress Resultants F1, M1, M2, M3')
		WRITE(EIN,'(1x,4ES20.10)') force_1D(1), force_1D(4), force_1D(5), force_1D(6)
    
		IF(Timoshenko_I==1) THEN   !Read two more stress resultants along with distributed loads and their derivatives for Timoshenko model
			READ(in,*,IOSTAT=in_stat) force_1D(2),force_1D(3)
			IF(IOError('read stress resultants F2,F3',error)) GOTO 9999
			

			CALL TitlePrint(EIN, '1D Stress Resultants F2, F3')
			WRITE(EIN,'(1x,2ES20.10)') force_1D(2), force_1D(3)

			READ(in,*,IOSTAT=in_stat) load_1D
			IF(IOError('read distributed loads',error)) GOTO 9999
   		
			CALL TitlePrint(EIN, 'Distributed Loads')
			WRITE(EIN,'(1x,6ES20.10)') load_1D

			READ(in,*,IOSTAT=in_stat) load1_1D
			IF(IOError('read first derivative of distributed loads',error)) GOTO 9999
       		
			CALL TitlePrint(EIN, 'First Derivative of Distributed Loads')
			WRITE(EIN,'(1x,6ES20.10)') load1_1D


			READ(in,*,IOSTAT=in_stat) load2_1D
   		    IF(IOError('read second derivative of distributed loads',error)) GOTO 9999
		
			CALL TitlePrint(EIN, 'Second Derivative of Distributed Loads')
			WRITE(EIN,'(1x,6ES20.10)') load2_1D
		ENDIF
!-------------------------------------------------------------------
	ENDIF
    
	!Allocate disp_3D_F to hold nodal displacements
	!-------------------------------------------------------------------------------
	ALLOCATE(disp_3D_F(nnode,5),STAT=allo_stat)
	IF(MemoryError('disp_3D_F',error)) GOTO 9999

	!Allocate ss_F to hold stress/strain values at Guassian Points
	!--------------------------------------------------------------------------------
	ALLOCATE(ss_F(nelem*MAX_NODE_ELEM,26),STAT=allo_stat)
	IF(MemoryError('ss_F',error)) GOTO 9999


	!Allocate ss_nd_F to hold the stress/strain values at all the nodes
	!-------------------------------------------------------------------------------- 
	ALLOCATE(ss_nd_F(nelem*MAX_NODE_ELEM,26),STAT=allo_stat)
	IF(MemoryError('ss_nd_F',error)) GOTO 9999


	!Allocate ss_elem to hold the average stress/strain values at Gaussian points within one element
	!-------------------------------------------------------------------------------- 
	ALLOCATE(ss_elem(nelem,24),STAT=allo_stat)
	IF(MemoryError('ss_elem',error)) GOTO 9999


ENDIF


WRITE(*,*) 'The inputs are echoed in ',TRIM(ech_name)
CLOSE(IN)
CLOSE(EIN)

9999 IF(error/='')THEN
    	IF(ALLOCATED(ss_elem)) DEALLOCATE(ss_elem)
		IF(ALLOCATED(ss_F)) DEALLOCATE(ss_F)
		IF(ALLOCATED(ss_nd_F)) DEALLOCATE(ss_nd_F)
		IF(ALLOCATED(disp_3D_F)) DEALLOCATE(disp_3D_F)
		IF(ALLOCATED(temperature)) DEALLOCATE(temperature)
		IF(ALLOCATED(cte)) DEALLOCATE(cte)
		IF(ALLOCATED(density)) DEALLOCATE(density)
		IF(ALLOCATED(material)) DEALLOCATE(material)
		IF(ALLOCATED(orth)) DEALLOCATE(orth)
		IF(ALLOCATED(mat_type_layer)) DEALLOCATE(mat_type_layer)
		IF(ALLOCATED(layup_angle)) 	 DEALLOCATE(layup_angle)
		IF(ALLOCATED(mat_type)) DEALLOCATE(mat_type)
		IF(ALLOCATED(layup)) 	 DEALLOCATE(layup)
		IF(ALLOCATED(elem_no_arr)) 	 DEALLOCATE(elem_no_arr)
		IF(ALLOCATED(element))	 DEALLOCATE(element)
		IF(ALLOCATED(node_no_arr)) 	 DEALLOCATE(node_no_arr)
		IF(ALLOCATED(coord)) 	 DEALLOCATE(coord)
	 ENDIF

END SUBROUTINE Input
!*****************************************



!************************************************************
!*                                                          *
!*    Output results from constitutive modeling             * 
!*															*
!************************************************************
SUBROUTINE Output


INTEGER:: i,j
REAL(DBL)::I11,radius_gyration


! Output the cross-sectional properties 
!====================================================
out_name=TRIM(inp_name) // ".K"
IF(FileOpen(OUT,  out_name,'REPLACE','WRITE',error))	 GOTO 9999

!==============================
! Output the mass matrix
!==============================
CALL TitlePrint(OUT, 'The 6X6 Mass Matrix')    
WRITE(OUT,'(1x,6ES20.10)')(mass(i,:),i=1,6)

CALL TitlePrint(OUT, 'The Mass Center of the Cross Section')    
WRITE(OUT,'(1x,A6, ES20.10)')' Xm2 =',xm2
WRITE(OUT,'(1x,A6, ES20.10)')' Xm3 =',xm3

!--------------------------------------------------------------------
! output the mass matrix at the mass center if the mass center is 
! not at the origin
!---------------------------------------------------------------------     
IF(ABS(xm2)>TOLERANCE.OR.ABS(xm3)>TOLERANCE) THEN

	CALL TitlePrint(OUT, 'The 6X6 Mass Matrix at the Mass Center')    
	WRITE(OUT,'(1x, 6ES20.12)')(mass_mc(i,:),i=1,6)

ENDIF

!--------------------------------------------------------------------
! output the mass properties at mass center with respect to the 
! principal inertial axes
!---------------------------------------------------------------------   
I11=I22+I33  
CALL TitlePrint(OUT, 'The Mass Properties with respect to Principal Inertial Axes')    
WRITE(OUT,'(1x,A40, ES20.10)')'Mass Per Unit Span                     =', mass_mc(1,1)
WRITE(OUT,'(1x,A40, ES20.10)')'Mass Moments of Intertia about x1 axis =', I11
WRITE(OUT,'(1x,A40, ES20.10)')'Mass Moments of Intertia about x2 axis =', I22
WRITE(OUT,'(1x,A40, ES20.10)')'Mass Moments of Intertia about x3 axis =', I33


IF(ABS(mass_angle)>TOLERANCE) THEN 
	WRITE(OUT,*)'The Principal Inertial Axes Rotated from User Coordinate System by '
	WRITE(OUT,'(1x, ES20.10)') mass_angle
	WRITE(OUT,*) 'Degree about the positive direction of x1 axis.'
ELSE 
	WRITE(OUT,*)'The user coordinate axes are the principal inertial axes.'
ENDIF
radius_gyration=sqrt((I22+I33)/mass_mc(1,1))
WRITE(OUT,'(1x,A40, ES20.10)')'The mass-weighted radius of gyration   = ', radius_gyration

    
CALL TitlePrint(OUT, 'The Geometric Center of the Cross Section')    
WRITE(OUT,'(1x,A6, ES20.10)')' Xg2 =',Xg2
WRITE(OUT,'(1x,A6, ES20.10)')' Xg3 =',Xg3

IF(Vlasov_I/=1)THEN
	CALL TitlePrint(OUT, 'Classical Stiffness Matrix (1-extension; 2-twist; 3,4-bending)')    
	WRITE(OUT,'(1x,4ES20.10)')(Aee(i,:),i=1,NE_1D)

	CALL TitlePrint(OUT, 'Classical Flexibility Matrix (1-extension; 2-twist; 3,4-bending)')    
	WRITE(OUT,'(1x,4ES20.10)')(Aee_F(i,:),i=1,NE_1D)

	IF(thermal_I==3)THEN 

		CALL TitlePrint(OUT, 'Nonmechanical Stress Resultants for Classical Model (1-extension; 2-twist; 3,4-bending)')    
		WRITE(OUT,'(1x,4ES20.10)')(NT(i),i=1,NE_1D)

		CALL TitlePrint(OUT, 'Thermal Strains for Classical Model (1-extension; 2-twist; 3,4-bending)')    
		WRITE(OUT,'(1x,4ES20.10)')(NT_F(i),i=1,NE_1D)

	ENDIF

ENDIF
CALL TitlePrint(OUT, 'The Neutral Axes (or Tension Center) of the Cross Section')    
WRITE(OUT,'(1x,A6, ES20.10)')' Xt2 =',Xe2
WRITE(OUT,'(1x,A6, ES20.10)')' Xt3 =',Xe3

IF(curved_I==1) THEN
	IF(Vlasov_I/=1)THEN
		CALL TitlePrint(OUT, 'Classical Stiffness Matrix (correct up to the 2nd order) (1-extension; 2-twist; 3,4-bending)')    
		WRITE(OUT,'(1x,4ES20.10)')(Aee_k(i,:),i=1,NE_1D)
	
		CALL TitlePrint(OUT, 'Classical Flexibility Matrix (correct up to the 2nd order) (1-extension; 2-twist; 3,4-bending)')    
		WRITE(OUT,'(1x,4ES20.10)')(Aee_k_F(i,:),i=1,NE_1D)

	ENDIF
	CALL TitlePrint(OUT, 'The Neutral Axes (or Tension Center) of the Cross Section, Corrected by Initial Curvature/Twist')    
	WRITE(OUT,'(1x,A6, ES20.10)')' Xt2 =',Xe2_k
	WRITE(OUT,'(1x,A6, ES20.10)')' Xt3 =',Xe3_k
ENDIF

IF(Timoshenko_I==1) THEN
	IF(Vlasov_I/=1)THEN
		CALL TitlePrint(OUT, 'Timoshenko Stiffness Matrix (1-extension; 2,3-shear, 4-twist; 5,6-bending)')    
		WRITE(OUT,'(1x,6ES20.10)')(ST(i,:),i=1,6)
    
		CALL TitlePrint(OUT, 'Timoshenko Flexibility Matrix (1-extension; 2,3-shear, 4-twist; 5,6-bending)')    
		WRITE(OUT,'(1x,6ES20.10)')(ST_F(i,:),i=1,6)
    ENDIF
    CALL TitlePrint(OUT, 'The Generalized Shear Center of the Cross Section in the User Coordinate System')    
    WRITE(OUT,'(1x,A6, ES20.10)')' Xs2 = ',Sc1
    WRITE(OUT,'(1x,A6, ES20.10)')' Xs3 = ',Sc2
ENDIF


IF(Vlasov_I==1) THEN
	CALL TitlePrint(OUT, 'Vlasov Stiffness Matrix (1-extension; 2-twist; 3,4-bending; 5-twist rate)')    
	WRITE(OUT,'(1x,5ES20.10)')(stiff_val(i,:),i=1,5)

	CALL TitlePrint(OUT, 'Vlasov Flexibility Matrix (1-extension; 2-twist; 3,4-bending; 5-twist rate)')    
	WRITE(OUT,'(1x,5ES20.10)')(stiff_val_F(i,:),i=1,5)
ENDIF


IF(trapeze_I==1) THEN
	CALL TitlePrint(OUT, 'Trapeze Effects Related Matrices')  
	CALL TitlePrint(OUT, 'Ag1--Ag1--Ag1--Ag1')    
	WRITE(OUT,'(1x,4ES20.10)')(Ag1(i,:),i=1,4)
     
	CALL TitlePrint(OUT, 'Bk1--Bk1--Bk1--Bk1')    
	WRITE(OUT,'(1x,4ES20.10)')(Bk1(i,:),i=1,4)
   	 
	CALL TitlePrint(OUT, 'Ck2--Ck2--Ck2--Ck2')    
	WRITE(OUT,'(1x,4ES20.10)')(Ck2(i,:),i=1,4)
     
	CALL TitlePrint(OUT, 'Dk3--Dk3--Dk3--Dk3')    
	WRITE(OUT,'(1x,4ES20.10)')(Dk3(i,:),i=1,4)
ENDIF


WRITE(*,*)
WRITE(*,*)'Cross-sectional properties can be found in  "',TRIM(out_name),'"'

CLOSE(OUT)



9999 RETURN

END SUBROUTINE Output
!************************************************************



!************************************************************
!*                                                          *
!*    Output the recovered 3D results                       *
!*															*
!************************************************************
SUBROUTINE RecoveryOutput

INTEGER:: i          

u_name=TRIM(inp_name)//".U"
IF(FileOpen(uout,  u_name,'REPLACE','WRITE',error))	 GOTO 9999		  
WRITE(uout,'(1x,i8,5ES20.10)')(i,disp_3D_F(i,:),i=1,nnode)

WRITE(*,*)'Recovered 3D displacement results are in ', TRIM(u_name)
CLOSE(uout)

e_name=TRIM(inp_name)//".E"
IF(FileOpen(eout,  e_name,'REPLACE','WRITE',error))	 GOTO 9999
WRITE(eout,'(1x,8ES20.10)')(ss_F(i,1:8), i=1,k_F)

s_name=TRIM(inp_name)//".S"
IF(FileOpen(sout,  s_name,'REPLACE','WRITE', error))	 GOTO 9999
WRITE(sout,'(1x,8ES20.10)')(ss_F(i,1:2), ss_F(i,9:14), i=1,k_F)
    	 
em_name=TRIM(inp_name)//".EM"
IF(FileOpen(emout,  em_name,'REPLACE','WRITE',error))	 GOTO 9999
WRITE(emout,'(1x,8ES20.10)')(ss_F(i,1:2), ss_F(i,15:20), i=1,k_F)

sm_name=TRIM(inp_name)//".SM"
IF(FileOpen(smout,  sm_name,'REPLACE','WRITE',error))	 GOTO 9999
WRITE(smout,'(1x,8ES20.10)')(ss_F(i,1:2), ss_F(i,21:26), i=1,k_F)

en_name=TRIM(inp_name)//".EN"
IF(FileOpen(enout,  en_name,'REPLACE','WRITE', error))	 GOTO 9999
WRITE(enout,'(1x,8ES20.10)')(ss_nd_F(i,1:8), i=1,nd_F)

sn_name=TRIM(inp_name)//".SN"
IF(FileOpen(snout,  sn_name,'REPLACE','WRITE',error))	 GOTO 9999
WRITE(snout,'(1x,8ES20.10)')(ss_nd_F(i,1:2), ss_nd_F(i,9:14), i=1,nd_F)

emn_name=TRIM(inp_name)//".EMN"
IF(FileOpen(emnout,  emn_name,'REPLACE','WRITE',error))	 GOTO 9999
WRITE(emnout,'(1x,8ES20.10)')(ss_nd_F(i,1:2), ss_nd_F(i,15:20),i=1,nd_F)
	
smn_name=TRIM(inp_name)//".SMN"
IF(FileOpen(smnout,  smn_name,'REPLACE','WRITE',error))	 GOTO 9999
WRITE(smnout,'(1x,8ES20.10)')(ss_nd_F(i,1:2), ss_nd_F(i,21:26),i=1,nd_F)

WRITE(*,*)'Recovered 3D strain results are in ', TRIM(e_name),'  ', TRIM(em_name), '  ', TRIM(en_name),'  ', TRIM(emn_name)
CLOSE(eout); CLOSE(emout); CLOSE(enout); CLOSE(emnout)

WRITE(*,*)'Recovered 3D stress results are in ', TRIM(s_name),'  ', TRIM(sm_name),'  ', TRIM(sn_name),'  ',TRIM(smn_name)
CLOSE(sout); CLOSE(smout); CLOSE(snout); CLOSE(smnout)


elem_name=TRIM(inp_name)//".ELE"
IF(FileOpen(elemout,  elem_name,'REPLACE','WRITE',error))	 GOTO 9999
WRITE(elemout,'(1x,i10,24ES20.10)')(i,ss_elem(i,:),i=1,nelem)

WRITE(*,*)'Recovered average 3D stresses/strains at Gaussian points within each element are in ', TRIM(elem_name)
CLOSE(elemout)

9999 RETURN

END SUBROUTINE RecoveryOutput
!********************************************************


!************************************************************
!*                                                          *
!*    Write error to the echo file                          *
!*															*
!************************************************************
SUBROUTINE WriteError

LOGICAL file_opened

INQUIRE (EIN,  OPENED = file_opened) ! Check whether the file is already opened, if yes, then dump the error message to this file

IF(file_opened)THEN

	WRITE(EIN,*) 
	IF(error/='')THEN

		CALL TitlePrint(EIN, 'Error Message')
		WRITE(EIN,'(1x, 300A)') error 

	ELSE

		WRITE(EIN,*) 'Congratulations! No errors!'
	ENDIF

	CLOSE(EIN)

ELSE 
	OPEN (UNIT=EIN, file=ech_name,STATUS='OLD',ACTION = 'WRITE',ACCESS='APPEND',IOSTAT=in_stat)
	IF(in_stat/=0) THEN
	   WRITE(*,*) 'Cannot open the file for writing error message'
	   RETURN
	ELSE 
		WRITE(EIN,*) 
		IF(error/='')THEN
			CALL TitlePrint(EIN, 'Error Message')
			WRITE(EIN,'(1x, 300A)') error 

		ELSE

			WRITE(EIN,*) 'Congratulations! No errors!'
		ENDIF

		CLOSE(EIN)
     ENDIF
ENDIF

END SUBROUTINE WriteError
!********************************************************




END MODULE VABSIO
!=========================================