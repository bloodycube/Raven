//Maya ASCII 2017 scene
//Name: eye_rig.ma
//Last modified: Tue, Nov 15, 2016 10:10:23 PM
//Codeset: 949
requires maya "2017";
requires "stereoCamera" "10.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201608291545-1001872";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	rename -uid "FFD0E39C-4744-494D-E3CC-FA8A0E356955";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 13.89754847809068 9.4263319676028967 7.8593279208954687 ;
	setAttr ".r" -type "double3" -32.138352729504355 57.800000000000246 5.9686550598874401e-015 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "059A20EA-431E-FBED-A89E-0EB1BFF819E5";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 18.889934587241012;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 1.1102230246251565e-015 0 2.7165 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "F3C65F9D-4316-E639-F983-A4B678351DC6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "62F6592B-49D5-D05A-B177-889B5FB8B80A";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "99D8B5B4-4653-EAA2-14D2-A3AB89F42D6E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "C5067641-4A0E-442A-A1FD-B28951378BBB";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "9300F122-46ED-4894-6CF4-87AC1DEEF87A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "E4208AD2-4F14-7861-3B57-81924A0B92C6";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 10.965517241379311;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode joint -n "eye_input";
	rename -uid "64FF8D81-4A4A-3809-FBA7-548F8B7AF2A1";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -89.999999999999986 0 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
createNode joint -n "eyeBall_input" -p "eye_input";
	rename -uid "0B733D7B-41EF-B2AE-89D8-33A8AAB4871F";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -4.89 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eyeBall";
	setAttr ".radi" 0.5;
createNode joint -n "iris_input" -p "eyeBall_input";
	rename -uid "A2B1B249-4864-7AD6-A81B-6C982A5D581A";
	setAttr ".t" -type "double3" 4.9999999999999991 0 -4.8985871965894138e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "iris";
	setAttr ".radi" 0.5;
createNode joint -n "upperLid_input" -p "eye_input";
	rename -uid "AF1E8190-428F-3522-5CC1-94B13FF47130";
	setAttr ".r" -type "double3" 0 0 -3.180554681463516e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 9.12 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "upperLid";
	setAttr ".radi" 0.5;
createNode joint -n "upperLidEnd_input" -p "upperLid_input";
	rename -uid "CB45EBF8-47BC-DE3A-AF8A-49BDBD7DD6B5";
	setAttr ".t" -type "double3" 5.0000000000000009 6.6613381477509392e-016 -4.8985871965894118e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "upperLidEnd";
	setAttr ".radi" 0.5;
createNode joint -n "lowerLid_input" -p "eye_input";
	rename -uid "56C5D7E3-4D15-4ADF-B05A-79A7AF5DB284";
	setAttr ".r" -type "double3" 0 0 3.180554681463516e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -20 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "lowerLid";
	setAttr ".radi" 0.5;
createNode joint -n "lowerLidEnd_input" -p "lowerLid_input";
	rename -uid "1060320D-462A-56F5-80B1-1BB70D491B1B";
	setAttr ".t" -type "double3" 5.0000000000000009 -6.6613381477509392e-016 -4.8985871965894118e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "lowerLidEnd";
	setAttr ".radi" 0.5;
createNode transform -n "const_grp" -p "eye_input";
	rename -uid "76187485-428C-CA3B-1B35-678A2C5E644E";
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
createNode parentConstraint -n "eyeBall_grp_parentConstraint1" -p "const_grp";
	rename -uid "BADA359B-40CD-6790-8088-8EB14C2345DE";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "eye_inputW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr ".r" -type "double3" 0 -89.999999999999986 0 ;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 -89.999999999999986 0 ;
	setAttr ".rsrr" -type "double3" 0 -89.999999999999986 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "eye_lookAtRig_grp_orientConstraint1" -p "const_grp";
	rename -uid "B0800877-4BB2-3E98-C551-98A91BB8A109";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "eyeBall_inputW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr ".r" -type "double3" 0 -89.999999999999986 0 ;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 -4.89 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "upperLid_zro_orientConstraint1" -p "const_grp";
	rename -uid "1677238D-478A-50F7-64F8-428725894F40";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "upperLid_inputW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr ".r" -type "double3" -89.999999999999957 -70.000000000000014 89.999999999999986 ;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 9.1199999999999974 ;
	setAttr ".rsrr" -type "double3" 0 0 20 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "lowerLid_zro_orientConstraint1" -p "const_grp";
	rename -uid "7667A404-421B-408B-60BE-A089313F0A88";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lowerLid_inputW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr ".r" -type "double3" 89.999999999999957 -70.000000000000014 -89.999999999999986 ;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999956 0.99999999999999967 0.99999999999999956 ;
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 -20 ;
	setAttr ".rsrr" -type "double3" 0 0 -20 ;
	setAttr -k on ".w0";
createNode pointConstraint -n "eyeLookAt_zro_pointConstraint1" -p "const_grp";
	rename -uid "9BF6DB48-40EE-9FFE-9FE7-99807FB91820";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "iris_inputW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" 3.7877895356746576e-015 -2.097966067790161 14.852559994102061 ;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr ".r" -type "double3" 90 -81.96 -90 ;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 10 0 0 ;
	setAttr ".rst" -type "double3" 5.0000000000000009 0 -4.8985871965894118e-016 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "null4_orientConstraint1" -p "const_grp";
	rename -uid "40A0C72D-411A-9A9F-FE8F-62A67C84CE53";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "eyeBall_inputW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "lowerLid_inputW1" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr ".r" -type "double3" 89.999999999999943 -75.98 -89.999999999999943 ;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 0 -12.445000000000002 ;
	setAttr ".rsrr" -type "double3" 0 0 -14.020000000000001 ;
	setAttr ".int" 2;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode joint -n "eye_output";
	rename -uid "4BFE705F-4CBD-30FB-BA9C-2E96924C06D6";
	setAttr ".t" -type "double3" 2.7001869743617619 0 -5.9956194994587297e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -89.999999999999986 0 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
createNode joint -n "eyeBall_output" -p "eye_output";
	rename -uid "5D7032B2-4D91-1C17-019A-6C85CB819C06";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eyeBall";
	setAttr ".radi" 0.5;
createNode joint -n "iris_output" -p "eyeBall_output";
	rename -uid "976C1CB3-44B3-46E6-E711-E7B91EBB7737";
	setAttr ".t" -type "double3" 4.9999999999999991 0 -4.8985871965894138e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "iris";
	setAttr ".radi" 0.5;
createNode orientConstraint -n "eyeBall_L_jnt_orientConstraint1" -p "eyeBall_output";
	rename -uid "035A2AA9-48A1-D8F3-E07C-238874EC3F5A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "eye_constJnt_outW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 -4.89 ;
	setAttr -k on ".w0";
createNode joint -n "upperLid_output" -p "eye_output";
	rename -uid "15429355-4069-2FA3-4413-F1B20EC27D53";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.3728319179984852e-016 2.4799562156788863e-015 19.999999999999996 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "upperLid";
	setAttr ".radi" 0.5;
createNode joint -n "upperLidEnd_output" -p "upperLid_output";
	rename -uid "F8640117-44E0-C07E-816B-F3919335EC52";
	setAttr ".t" -type "double3" 5.0000000000000009 6.6613381477509392e-016 -4.8985871965894118e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "upperLidEnd";
	setAttr ".radi" 0.5;
createNode orientConstraint -n "upperLid_L_jnt_orientConstraint1" -p "upperLid_output";
	rename -uid "8F4134A2-4CF6-FBA0-A7DA-20BE57A94805";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "upperLid_FK__SIDE__ctrlW0" -dv 1 
		-min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "upperLid_constJnt_outW1" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 0 -10.880000000000003 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode joint -n "lowerLid_output" -p "eye_output";
	rename -uid "6D5291E9-4130-C789-73A8-65ABF35DFDB9";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.3728319179984852e-016 2.4799562156788863e-015 -19.999999999999996 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "lowerLid";
	setAttr ".radi" 0.5;
createNode joint -n "lowerLidEnd_output" -p "lowerLid_output";
	rename -uid "FC16CFF6-42D3-B8ED-BFBA-92AF6806357B";
	setAttr ".t" -type "double3" 5.0000000000000009 -6.6613381477509392e-016 -4.8985871965894118e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "lowerLidEnd";
	setAttr ".radi" 0.5;
createNode orientConstraint -n "lowerLid_L_jnt_orientConstraint1" -p "lowerLid_output";
	rename -uid "7B6CA9C7-473A-4422-61A2-818E07880711";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lowerLid_FK__SIDE__ctrlW0" -dv 1 
		-min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "lowerLid_constJnt_outW1" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 0 3.180554681463516e-015 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "eyeBall_grp";
	rename -uid "80BDD328-4D06-95DA-CD4B-69ACD779C245";
createNode transform -n "eye_zro" -p "eyeBall_grp";
	rename -uid "65DF5A23-41D1-88EF-25DD-06BC99AE1961";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
createNode transform -n "eye_lookAt" -p "|eyeBall_grp|eye_zro";
	rename -uid "804EA34D-43D7-BABA-2E10-D8AB053AE747";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0.47399998 ;
createNode transform -n "eye_FK_ctrl" -p "eye_lookAt";
	rename -uid "046F6EEE-4DD0-3A9C-B3D6-22BC8F155B79";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 1 0 ;
createNode nurbsCurve -n "eye_FK_ctrlShape" -p "eye_FK_ctrl";
	rename -uid "418AC2DE-4BB0-1A73-E1B4-4EAA361AEAFD";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		5 0.39180581244561252 -0.39180581244561247
		5 -6.3215853039146618e-017 -0.55409709377719452
		5 -0.39180581244561213 -0.39180581244561269
		5 -0.55409709377719396 -7.2881813321918902e-016
		5 -0.39180581244561224 0.39180581244561147
		5 -1.6696026817952597e-016 0.55409709377719363
		5 0.39180581244561191 0.39180581244561163
		5 0.55409709377719396 -2.7064802789329827e-016
		5 0.39180581244561252 -0.39180581244561247
		5 -6.3215853039146618e-017 -0.55409709377719452
		5 -0.39180581244561213 -0.39180581244561269
		;
createNode transform -n "const_eyeJnt" -p "eye_FK_ctrl";
	rename -uid "6C188C9D-4B1F-4673-406E-49A543EC2C4D";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode orientConstraint -n "eye_zro_orientConstraint1" -p "|eyeBall_grp|eye_zro";
	rename -uid "26568389-4CA3-1053-1BFD-07B32CE439CB";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "eyeBall_inputW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 -4.89 ;
	setAttr -k on ".w0";
createNode transform -n "upperLid_zro" -p "eyeBall_grp";
	rename -uid "49488C88-41C3-7436-50E8-848B0372842B";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
createNode transform -n "upperLid_autoFollow" -p "|eyeBall_grp|upperLid_zro";
	rename -uid "98B8EBB0-4759-9B7A-9107-D7B448915FBD";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".s" -type "double3" 0.99999999999999989 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "upperLid_autoClose" -p "upperLid_autoFollow";
	rename -uid "0FF236E3-4D66-604F-D586-7798D9BB56A1";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000004 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 1 1 ;
createNode orientConstraint -n "upperLid_autoClose_orientConstraint1" -p "upperLid_autoClose";
	rename -uid "C5F0C383-41BD-DF5B-3055-9096B2657793";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "upperLid_const_outW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 -1.5902773407317584e-015 ;
	setAttr ".rsrr" -type "double3" 0 0 5.862332965158866 ;
	setAttr ".int" 2;
	setAttr ".hio" yes;
	setAttr -k on ".w0";
createNode transform -n "upperLid_FK_ctrl" -p "upperLid_autoClose";
	rename -uid "6762863C-4BA5-7F9C-D584-FC887A90E929";
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999989 0.99999999999999956 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 1 0 ;
createNode nurbsCurve -n "upperLid_FK_ctrlShape" -p "upperLid_FK_ctrl";
	rename -uid "A83E587C-46AD-D748-DB28-E896D5880014";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.9999998859205448 0.39180591076049731 -0.39180581244561241
		4.9999998859205448 9.8314884725625683e-008 -0.55409709377719452
		4.9999998859205448 -0.39180571413072734 -0.39180581244561263
		4.9999998859205448 -0.55409699546230917 -6.733069819879312e-016
		4.9999998859205448 -0.39180571413072746 0.39180581244561152
		4.9999998859205448 9.8314884621881273e-008 0.55409709377719363
		4.9999998859205448 0.3918059107604967 0.39180581244561169
		4.9999998859205448 0.55409719209207875 -2.1513687666204044e-016
		4.9999998859205448 0.39180591076049731 -0.39180581244561241
		4.9999998859205448 9.8314884725625683e-008 -0.55409709377719452
		4.9999998859205448 -0.39180571413072734 -0.39180581244561263
		;
createNode transform -n "const_upperLidJnt" -p "upperLid_FK_ctrl";
	rename -uid "05CBF418-49FC-2AD0-1869-80AAE82B625C";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode transform -n "lowerLid_zro" -p "eyeBall_grp";
	rename -uid "2F14F88A-43E1-C41F-E141-58AF537B6BCE";
	setAttr ".s" -type "double3" 0.99999999999999956 0.99999999999999967 0.99999999999999956 ;
createNode transform -n "lowerLid_autoFollow" -p "|eyeBall_grp|lowerLid_zro";
	rename -uid "52D7405D-4326-DCE4-68B0-49AD33EAB214";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000004 1.0000000000000004 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "lowerLid_autoClose" -p "lowerLid_autoFollow";
	rename -uid "24AC4D36-44D3-ED9E-1AE3-A2B7B08C036C";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000004 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 1 1 ;
createNode orientConstraint -n "lowerLid_autoClose_orientConstraint1" -p "lowerLid_autoClose";
	rename -uid "9CE53EA4-4383-8605-2AB7-1EBCF54720BC";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lowerLid_const_outW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 -1.2722218725854067e-014 ;
	setAttr ".rsrr" -type "double3" 0 0 4.1214284852567769 ;
	setAttr ".int" 2;
	setAttr ".hio" yes;
	setAttr -k on ".w0";
createNode transform -n "lowerLid_FK_ctrl" -p "lowerLid_autoClose";
	rename -uid "BFBCAE67-4821-2878-0E80-14BC81229394";
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999944 0.99999999999999933 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 1 0 ;
createNode nurbsCurve -n "lowerLid_FK_ctrlShape" -p "lowerLid_FK_ctrl";
	rename -uid "EF8BFE68-4F7F-4820-0FEA-BF9B93A0B93C";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.9999998859205448 0.39180571413072762 -0.39180581244561241
		4.9999998859205448 -9.8314884963079697e-008 -0.55409709377719452
		4.9999998859205448 -0.39180591076049703 -0.39180581244561263
		4.9999998859205448 -0.55409719209207886 -6.733069819879312e-016
		4.9999998859205448 -0.39180591076049714 0.39180581244561152
		4.9999998859205448 -9.8314885066824107e-008 0.55409709377719363
		4.9999998859205448 0.39180571413072701 0.39180581244561169
		4.9999998859205448 0.55409699546230906 -2.1513687666204044e-016
		4.9999998859205448 0.39180571413072762 -0.39180581244561241
		4.9999998859205448 -9.8314884963079697e-008 -0.55409709377719452
		4.9999998859205448 -0.39180591076049703 -0.39180581244561263
		;
createNode transform -n "const_lowerLidJnt" -p "lowerLid_FK_ctrl";
	rename -uid "F4667C45-4A9E-7779-49E1-209B21A69CC1";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode transform -n "eye_lookAtRig_grp" -p "eyeBall_grp";
	rename -uid "E467E2C9-4DDF-BFDA-BCD9-879925A1AFFE";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0.47399998 ;
createNode transform -n "lookAt_out" -p "eye_lookAtRig_grp";
	rename -uid "7ABA3D83-4F93-52F2-BD4F-9FA65C9213ED";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode aimConstraint -n "null3_aimConstraint1" -p "lookAt_out";
	rename -uid "527A8949-4260-254F-3547-E681A23D5C59";
	addAttr -dcb 0 -ci true -sn "w0" -ln "eyeLookAt__SIDE__ctrlW0" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "eyeLookAt_zro" -p "eye_lookAtRig_grp";
	rename -uid "74D00D1D-4898-0400-7B08-3D88ABF39D78";
createNode transform -n "eyeLookAt__SIDE__ctrl" -p "eyeLookAt_zro";
	rename -uid "6F493AEA-404C-879F-237D-08A0B5D45232";
createNode nurbsCurve -n "eyeLookAt__SIDE__ctrlShape" -p "eyeLookAt__SIDE__ctrl";
	rename -uid "570B866B-499B-E840-E79B-9EAFFBBE0375";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.2601436025374922e-016 0.78361162489122504 -0.78361162489122382
		-6.7857323231109159e-017 -1.2643170607829324e-016 -1.1081941875543879
		-2.2197910707351845e-016 -0.78361162489122427 -0.78361162489122427
		-2.4606854055573011e-016 -1.1081941875543879 -3.2112695072372299e-016
		-1.2601436025374907e-016 -0.78361162489122449 0.78361162489122405
		6.7857323231109072e-017 -3.3392053635905195e-016 1.1081941875543881
		2.2197910707351835e-016 0.78361162489122382 0.78361162489122438
		2.4606854055573016e-016 1.1081941875543879 5.9521325992805852e-016
		1.2601436025374922e-016 0.78361162489122504 -0.78361162489122382
		-6.7857323231109159e-017 -1.2643170607829324e-016 -1.1081941875543879
		-2.2197910707351845e-016 -0.78361162489122427 -0.78361162489122427
		;
createNode transform -n "lid_autoCloseRig_grp" -p "eyeBall_grp";
	rename -uid "47D960F7-4904-5D81-9AC4-4B85B79C5B6D";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 1 1 ;
createNode transform -n "null4" -p "lid_autoCloseRig_grp";
	rename -uid "2241324F-4FF2-BA4A-0C53-AF85EB8B4315";
createNode transform -n "close_tgt_driver" -p "null4";
	rename -uid "05067754-4EC0-FA22-3E1F-DEB33B1A18AE";
createNode aimConstraint -n "close_tgt_aimConstraint1" -p "close_tgt_driver";
	rename -uid "78BF8DE0-42E7-40A9-9B32-9F99D2785D23";
	addAttr -dcb 0 -ci true -sn "w0" -ln "closePoint_ctrlW0" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rsrr" -type "double3" 9.6641230122796005e-016 -1.257276816737561e-014 
		-8.7908533809463272 ;
	setAttr -k on ".w0";
createNode transform -n "eyeClose_ctrl_zro" -p "lid_autoCloseRig_grp";
	rename -uid "489056EA-4C33-71BF-CBB5-C2A39925AAE6";
	setAttr ".t" -type "double3" 6 0 1.3322676295501875e-015 ;
createNode transform -n "eyeClose_ctrl" -p "eyeClose_ctrl_zro";
	rename -uid "BA87BBCC-47A4-1912-82A1-E38588BB9C01";
	addAttr -ci true -sn "close" -ln "close" -min 0 -max 1 -at "double";
	setAttr ".t" -type "double3" 0.61195536616667834 -1.5015081747059464 3.6885950663127333e-015 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".close";
createNode nurbsCurve -n "eyeClose_ctrlShape" -p "eyeClose_ctrl";
	rename -uid "2F8F3003-4B47-7FCC-FF99-98B4B7EAE17E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		-2.2204460492503131e-016 0 1.0000000000000002
		2.2204460492503131e-016 0 -1.0000000000000002
		;
createNode transform -n "consted_lowerLid_autoFollow" -p "lid_autoCloseRig_grp";
	rename -uid "6EFF8C7F-45C0-853E-C0E5-608849985558";
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999989 1 ;
createNode orientConstraint -n "upperLid_tgt_orientConstraint1" -p "consted_lowerLid_autoFollow";
	rename -uid "9BB19039-4A52-BC95-7328-ECBD340C0BF2";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "upperLid_autoFollowW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 9.1199999999999921 ;
	setAttr ".rsrr" -type "double3" 0 0 20 ;
	setAttr -k on ".w0";
createNode transform -n "consted_upperLid_autoFollow" -p "lid_autoCloseRig_grp";
	rename -uid "A513759A-4A3D-9124-0AD5-DD971069C906";
createNode orientConstraint -n "lowerLid_tgt_orientConstraint1" -p "consted_upperLid_autoFollow";
	rename -uid "BD57AE60-4B55-83D5-0701-888552F97B36";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lowerLid_autoFollowW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 -19.999999999999996 ;
	setAttr ".rsrr" -type "double3" 0 0 -20 ;
	setAttr -k on ".w0";
createNode transform -n "upperLid_const_out" -p "lid_autoCloseRig_grp";
	rename -uid "065289CE-458B-8296-EB22-EDBEE4900056";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode orientConstraint -n "upperLid_const_orientConstraint1" -p "upperLid_const_out";
	rename -uid "755685CF-41A7-1510-7138-B1978AE09C73";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "close_tgtW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "upperLid_tgtW1" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 0 9.1199999999999903 ;
	setAttr ".rsrr" -type "double3" 0 0 3.8818303068517372 ;
	setAttr ".int" 2;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "locator1" -p "upperLid_const_out";
	rename -uid "3404A39B-450E-995C-5E6C-CB9C45A39614";
	setAttr ".t" -type "double3" 3 0 0 ;
createNode locator -n "locatorShape1" -p "locator1";
	rename -uid "B81F46F9-4F0D-6941-BA11-9FB5E832AA5C";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 3 0 0 ;
createNode transform -n "lowerLid_const_out" -p "lid_autoCloseRig_grp";
	rename -uid "42A45A22-46F3-C982-A34E-329E5F6E7555";
	setAttr ".s" -type "double3" 1.0000000000000002 1 1 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode orientConstraint -n "lowerLid_const_orientConstraint1" -p "lowerLid_const_out";
	rename -uid "D8B33543-4AB1-F109-C372-A982C0A001E9";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "close_tgtW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "lowerLid_tgtW1" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 0 -20 ;
	setAttr ".rsrr" -type "double3" 0 0 -16.118169693148257 ;
	setAttr ".int" 2;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "locator2" -p "lowerLid_const_out";
	rename -uid "F8764F2C-4069-E8A4-034A-7597ECF92F36";
	setAttr ".t" -type "double3" 3 0 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 0.99999999999999989 ;
createNode locator -n "locatorShape2" -p "locator2";
	rename -uid "87948DA2-4FD7-831E-7D6E-C898089728BF";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 3 0 0 ;
createNode transform -n "lid_autoFollowRig_grp" -p "eyeBall_grp";
	rename -uid "DA8991E1-4ED1-5C10-9D61-47A09CF7F216";
	setAttr ".v" no;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "eye_zro" -p "lid_autoFollowRig_grp";
	rename -uid "A909D761-48E5-BA29-74CB-BA98DB356F8B";
createNode transform -n "eye_rotation" -p "|eyeBall_grp|lid_autoFollowRig_grp|eye_zro";
	rename -uid "88DEBBC1-4777-9671-50D6-FDB6E946D553";
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1 ;
createNode transform -n "locator5" -p "eye_rotation";
	rename -uid "F66553E5-4E98-D612-D386-41A9F19CBD98";
	setAttr ".t" -type "double3" 3 0 0 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1.0000000000000002 ;
createNode locator -n "locatorShape5" -p "locator5";
	rename -uid "948C85C3-4689-7282-4EE0-22A0B6320BA9";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 3 0 0 ;
createNode orientConstraint -n "eye_rotation_orientConstraint1" -p "eye_rotation";
	rename -uid "CAA3AF3C-4EF7-6F5B-15F7-BCA432C255E3";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "const_eyeJntW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".int" 2;
	setAttr -k on ".w0";
createNode transform -n "upperLid_const" -p "|eyeBall_grp|lid_autoFollowRig_grp|eye_zro";
	rename -uid "EBE1A7DF-4DA8-44F2-373E-3D89493AF721";
	setAttr ".s" -type "double3" 0.99999999999999978 1 1 ;
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode transform -n "locator3" -p "upperLid_const";
	rename -uid "0DD5B81A-4E53-2D58-0D66-9DBDC105E9A5";
	setAttr ".t" -type "double3" 3 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000004 1.0000000000000004 1.0000000000000002 ;
createNode locator -n "locatorShape3" -p "locator3";
	rename -uid "E6F17127-42D9-AB71-2E79-B3BE005AAB13";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 3 0 0 ;
createNode orientConstraint -n "upperLid_const_orientConstraint2" -p "upperLid_const";
	rename -uid "05B83A09-4C51-272B-0D09-589EC69C29B8";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "eye_rotationW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "eye_zroW1" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".rsrr" -type "double3" 0 0 -29.248262526620721 ;
	setAttr ".int" 2;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "lowerLid_const" -p "|eyeBall_grp|lid_autoFollowRig_grp|eye_zro";
	rename -uid "F6E2B433-42A1-670E-812F-949CB3481B09";
	setAttr ".mrze" yes;
	setAttr ".xrze" yes;
createNode transform -n "locator4" -p "lowerLid_const";
	rename -uid "F7F4E219-45C8-FDA8-D140-D38947B17E04";
	setAttr ".t" -type "double3" 3 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
createNode locator -n "locatorShape4" -p "locator4";
	rename -uid "83E5483F-4241-DC7E-2525-ACA31A4380E2";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 3 0 0 ;
createNode orientConstraint -n "lowerLid_const_orientConstraint2" -p "lowerLid_const";
	rename -uid "A153C7C8-4108-4652-79C2-E29C66A68BE5";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "eye_rotationW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "eye_zroW1" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".rsrr" -type "double3" 0 0 10.751737473379274 ;
	setAttr ".int" 2;
	setAttr -k on ".w0" 0.3;
	setAttr -k on ".w1";
createNode transform -n "upperLid_zro" -p "lid_autoFollowRig_grp";
	rename -uid "368E7BB1-48DF-5C9C-471C-8687394FFF9E";
createNode transform -n "upperLid_autoFollow_max" -p "|eyeBall_grp|lid_autoFollowRig_grp|upperLid_zro";
	rename -uid "88665D6B-498E-0B21-D71F-DD9AEA76E204";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 0 13.032285476224567 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr ".s" -type "double3" 0.99999999999999989 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "upperLid_autoFollow_maxShape" -p "upperLid_autoFollow_max";
	rename -uid "20F1BA20-4BAF-35E7-6698-92B0741A9E77";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 23;
	setAttr ".cc" -type "nurbsCurve" 
		1 3 0 no 3
		4 0 1 2 3
		4
		0 0 0
		3 0 0
		3 -2.2204460492503131e-016 -0.99999999999999956
		3 0 -1.6653345369377348e-016
		;
createNode transform -n "upperLid_autoFollow_min" -p "|eyeBall_grp|lid_autoFollowRig_grp|upperLid_zro";
	rename -uid "EFE425D0-4074-037A-867D-F089A0107546";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 0 -40.274723100251258 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr ".s" -type "double3" 0.99999999999999989 1.0000000000000002 1.0000000000000002 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "upperLid_autoFollow_minShape" -p "upperLid_autoFollow_min";
	rename -uid "B6649528-4604-9B57-A836-F1ADA42427CE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 23;
	setAttr ".cc" -type "nurbsCurve" 
		1 3 0 no 3
		4 0 1 2 3
		4
		0 0 0
		3 0 0
		3 1.1102230246251575e-016 1.0000000000000009
		3 0 -1.6653345369377348e-016
		;
createNode transform -n "curve1" -p "|eyeBall_grp|lid_autoFollowRig_grp|upperLid_zro";
	rename -uid "9F8BD3EF-4FCE-6AC4-FEA7-C698A6BB9E19";
createNode nurbsCurve -n "curveShape1" -p "curve1";
	rename -uid "FD52A23F-4A6A-26A2-AA86-BEA2B264F26E";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		4 0 0
		;
createNode transform -n "lowerLid_zro" -p "lid_autoFollowRig_grp";
	rename -uid "2FC67DC9-4C77-05C9-CA83-93B94925543A";
createNode transform -n "lowerLid_autoFollow_max" -p "|eyeBall_grp|lid_autoFollowRig_grp|lowerLid_zro";
	rename -uid "CECE6055-49D0-30A8-E7E6-8184FC7123DC";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 0 16.092978628285408 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "lowerLid_autoFollow_maxShape" -p "lowerLid_autoFollow_max";
	rename -uid "3E8E183D-452C-81AA-1A20-C58ED24EEA48";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
	setAttr ".cc" -type "nurbsCurve" 
		1 3 0 no 3
		4 0 1 2 3
		4
		0 0 0
		3 0 0
		3.0000000000000004 -1.1102230246251565e-016 7.2164496600635175e-016
		2.9999999999999996 1.9428902930940239e-016 -1
		;
createNode transform -n "lowerLid_autoFollow_min" -p "|eyeBall_grp|lid_autoFollowRig_grp|lowerLid_zro";
	rename -uid "F1FB623A-413B-4B6A-85F7-0EAC369708BC";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 0 -12.072978900612965 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "lowerLid_autoFollow_minShape" -p "lowerLid_autoFollow_min";
	rename -uid "5CA63D45-402A-6B0E-A1B2-9B915E492C36";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 15;
	setAttr ".cc" -type "nurbsCurve" 
		1 3 0 no 3
		4 0 1 2 3
		4
		0 0 0
		3 0 0
		3 0 -1.6653345369377348e-016
		2.9999999999999996 0 1.0000000000000009
		;
createNode transform -n "curve2" -p "|eyeBall_grp|lid_autoFollowRig_grp|lowerLid_zro";
	rename -uid "BA595654-4454-E317-E5A2-6DBDD90CE5C5";
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
createNode nurbsCurve -n "curveShape2" -p "curve2";
	rename -uid "DE12032D-4CBB-0015-0599-8683F7403630";
	setAttr -k off ".v";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		4 0 0
		;
createNode transform -n "nurbsCircle1";
	rename -uid "0F735556-4069-362C-5831-54BDCB5193A3";
	setAttr ".s" -type "double3" 5 5 5 ;
createNode nurbsCurve -n "nurbsCircleShape1" -p "nurbsCircle1";
	rename -uid "50A310DD-4EFC-1BB0-B7EE-DBBED7DDAAA4";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "curve3";
	rename -uid "03637E9A-449A-144C-6CB9-3E956865C00D";
createNode nurbsCurve -n "curveShape3" -p "curve3";
	rename -uid "F2326AEA-4962-FDCD-4E7C-C6AF156BB70E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 0.09203405597
		2
		-6 0 -1
		-4.8955913283600001 0 -1
		;
createNode transform -n "curve4";
	rename -uid "A267F4CE-4AFE-66D9-2C02-529B2CE44F7D";
createNode nurbsCurve -n "curveShape4" -p "curve4";
	rename -uid "82E3296C-4369-8C61-B662-458E3701F5B7";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 0.09203405597
		2
		-6 0 1
		-4.8955913283600001 0 1
		;
createNode transform -n "curve3detachedCurve2";
	rename -uid "52BF524C-45B4-1711-3F8D-A08869596AC2";
createNode nurbsCurve -n "curve3detachedCurveShape2" -p "curve3detachedCurve2";
	rename -uid "B87669C4-4EBB-CC3F-8538-958325080F8E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0.09203405597 0.90796594399999997
		2
		-4.8955913283600001 0 -1
		4.8955913279999992 0 -1
		;
createNode transform -n "curve3detachedCurve3";
	rename -uid "2ABBF6A6-4B1D-B6DF-174E-BDA979CB8327";
createNode nurbsCurve -n "curve3detachedCurveShape3" -p "curve3detachedCurve3";
	rename -uid "CD09E531-489C-C3C6-BC74-23A0B21209FC";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0.90796594399999997 1
		2
		4.8955913280000001 0 -1
		6 0 -1
		;
createNode transform -n "curve4detachedCurve2";
	rename -uid "E47D859A-43C5-3C31-B782-FCABBF6D630C";
createNode nurbsCurve -n "curve4detachedCurveShape2" -p "curve4detachedCurve2";
	rename -uid "42AADC62-473D-12D6-1273-2EAC6B9337E3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0.09203405597 0.90796594399999997
		2
		-4.8955913283600001 0 1
		4.8955913279999992 0 1
		;
createNode transform -n "curve4detachedCurve3";
	rename -uid "36B6CDEE-4FEA-D655-7E68-FDBDF0D48D01";
createNode nurbsCurve -n "curve4detachedCurveShape3" -p "curve4detachedCurve3";
	rename -uid "DEAFB779-4C51-7B38-F7A5-ACA7668F611F";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0.90796594399999997 1
		2
		4.8955913280000001 0 1
		6 0 1
		;
createNode transform -n "detachedCurve1";
	rename -uid "5369BD17-418D-558F-465B-04836E58C6A3";
	setAttr ".s" -type "double3" 5 5 5 ;
createNode nurbsCurve -n "detachedCurveShape1" -p "detachedCurve1";
	rename -uid "9ACCF7DC-4BC3-1226-AB9D-3DBBF444101B";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "detachedCurve2";
	rename -uid "67F2FC87-4DC1-FB83-FBAC-1D8C2DB0BEFF";
	setAttr ".s" -type "double3" 5 5 5 ;
createNode nurbsCurve -n "detachedCurveShape2" -p "detachedCurve2";
	rename -uid "E3D001CE-4535-D473-1455-47A0C71AE94C";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "detachedCurve3";
	rename -uid "CA757213-4E40-D5E1-C652-E3BC47DEA8B5";
	setAttr ".s" -type "double3" 5 5 5 ;
createNode nurbsCurve -n "detachedCurveShape3" -p "detachedCurve3";
	rename -uid "2C418374-44E7-9C56-7B74-588DA6890AB6";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "4F161C8A-4D4C-47A4-E51D-DDA5452C18BC";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "EEA5BC2B-45EA-25FC-B157-CC8777235A90";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "A5F5B55C-4CDC-E400-FC7D-E2BD5F33FD0E";
createNode displayLayerManager -n "layerManager";
	rename -uid "7496580E-4A0D-31BD-5650-478243956631";
	setAttr ".dli[1]"  1;
	setAttr -s 2 ".dli";
createNode displayLayer -n "defaultLayer";
	rename -uid "42FC816F-4BE2-7C5D-5A4B-868BAC6EEACD";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "1038692D-423B-580E-0E2B-C49DF3A12940";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "7AD116BA-4A4B-F8A2-8B70-709DF06CE352";
	setAttr ".g" yes;
createNode animCurveUU -n "upperLid_const_orientConstraint1_upperLid_tgtW1";
	rename -uid "78EAC86D-4B5D-5F2E-DC69-60BD21DFD44F";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  0 1 1 0;
createNode animCurveUU -n "lowerLid_const_orientConstraint1_lowerLid_tgtW1";
	rename -uid "A058B095-41EF-DBB1-87B8-A4BF3333F094";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  0 1 1 0;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "A6C7D88A-4EB8-0D85-EBA5-54B1224301FF";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -docTag \"RADRENDER\" \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n"
		+ "                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n"
		+ "                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n"
		+ "                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 698\n                -height 877\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n"
		+ "            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n"
		+ "            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 698\n            -height 877\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 698\\n    -height 877\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 698\\n    -height 877\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "AC221762-45FB-7176-B55D-E4B5449A3DBD";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "9F3A22C1-4663-7256-579D-678BD87C3F02";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2746.6844573707203 -101.28352051940396 ;
	setAttr ".tgi[0].vh" -type "double2" -167.0224768825496 1226.9352968152791 ;
	setAttr -s 14 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -940;
	setAttr ".tgi[0].ni[0].y" 811.4285888671875;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" -441.42855834960937;
	setAttr ".tgi[0].ni[1].y" 525.71429443359375;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" -441.42855834960937;
	setAttr ".tgi[0].ni[2].y" 627.14288330078125;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" -1324.2857666015625;
	setAttr ".tgi[0].ni[3].y" 128.57142639160156;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" -441.42855834960937;
	setAttr ".tgi[0].ni[4].y" 424.28570556640625;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" -21.372348785400391;
	setAttr ".tgi[0].ni[5].y" 698.81646728515625;
	setAttr ".tgi[0].ni[5].nvs" 18306;
	setAttr ".tgi[0].ni[6].x" -1324.2857666015625;
	setAttr ".tgi[0].ni[6].y" 230;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" -441.42855834960937;
	setAttr ".tgi[0].ni[7].y" 282.85714721679687;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" -94.285713195800781;
	setAttr ".tgi[0].ni[8].y" 144.28572082519531;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" -1324.2857666015625;
	setAttr ".tgi[0].ni[9].y" 887.14288330078125;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" -940;
	setAttr ".tgi[0].ni[10].y" 450;
	setAttr ".tgi[0].ni[10].nvs" 19906;
	setAttr ".tgi[0].ni[11].x" -940;
	setAttr ".tgi[0].ni[11].y" 710;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" -940;
	setAttr ".tgi[0].ni[12].y" 608.5714111328125;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" -2239.30810546875;
	setAttr ".tgi[0].ni[13].y" 725.6868896484375;
	setAttr ".tgi[0].ni[13].nvs" 21490;
createNode animCurveUU -n "upperLid_const_orientConstraint2_eye_zroW1";
	rename -uid "F1F39E9C-4737-0CE9-ED3C-F8852AAF4A9A";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  0 1 1 0;
createNode animCurveUU -n "lowerLid_const_orientConstraint2_eye_zroW1";
	rename -uid "3AB8C39E-4A0E-D9A0-2B89-18AB56A266EA";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  0 1 1 0;
createNode displayLayer -n "layer1";
	rename -uid "B8B1F573-4E95-331F-2BD8-75A0AE3A56FD";
	setAttr ".c" 17;
	setAttr ".do" 1;
createNode makeNurbCircle -n "makeNurbCircle1";
	rename -uid "05F707CC-4DB4-8E59-FBD8-228A1AA44061";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode detachCurve -n "detachCurve1";
	rename -uid "2A8F6928-4582-424F-7F08-61BFAB32C551";
	setAttr -s 4 ".oc";
	setAttr -s 4 ".p[0:3]"  1.7431165310000001 2.2568834689999999 5.7431165310000001 
		6.2568834689999999;
	setAttr -s 5 ".k[0:4]" yes yes yes yes yes;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 1;
	setAttr -av ".unw" 1;
	setAttr -k on ".etw";
	setAttr -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -k on ".ihi";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -k on ".mbsof";
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".w";
	setAttr -av ".h";
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr -av ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off ".eeaa";
	setAttr -k off ".engm";
	setAttr -k off ".mes";
	setAttr -k off ".emb";
	setAttr -av -k off ".mbbf";
	setAttr -k off ".mbs";
	setAttr -k off ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off ".twa";
	setAttr -k off ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "layer1.di" "eye_input.do";
connectAttr "eye_input.s" "eyeBall_input.is";
connectAttr "eyeBall_input.s" "iris_input.is";
connectAttr "eye_input.s" "upperLid_input.is";
connectAttr "upperLid_input.s" "upperLidEnd_input.is";
connectAttr "eye_input.s" "lowerLid_input.is";
connectAttr "lowerLid_input.s" "lowerLidEnd_input.is";
connectAttr "eyeBall_grp.ro" "eyeBall_grp_parentConstraint1.cro";
connectAttr "eyeBall_grp.pim" "eyeBall_grp_parentConstraint1.cpim";
connectAttr "eyeBall_grp.rp" "eyeBall_grp_parentConstraint1.crp";
connectAttr "eyeBall_grp.rpt" "eyeBall_grp_parentConstraint1.crt";
connectAttr "eye_input.t" "eyeBall_grp_parentConstraint1.tg[0].tt";
connectAttr "eye_input.rp" "eyeBall_grp_parentConstraint1.tg[0].trp";
connectAttr "eye_input.rpt" "eyeBall_grp_parentConstraint1.tg[0].trt";
connectAttr "eye_input.r" "eyeBall_grp_parentConstraint1.tg[0].tr";
connectAttr "eye_input.ro" "eyeBall_grp_parentConstraint1.tg[0].tro";
connectAttr "eye_input.s" "eyeBall_grp_parentConstraint1.tg[0].ts";
connectAttr "eye_input.pm" "eyeBall_grp_parentConstraint1.tg[0].tpm";
connectAttr "eye_input.jo" "eyeBall_grp_parentConstraint1.tg[0].tjo";
connectAttr "eye_input.ssc" "eyeBall_grp_parentConstraint1.tg[0].tsc";
connectAttr "eye_input.is" "eyeBall_grp_parentConstraint1.tg[0].tis";
connectAttr "eyeBall_grp_parentConstraint1.w0" "eyeBall_grp_parentConstraint1.tg[0].tw"
		;
connectAttr "eye_lookAtRig_grp.ro" "eye_lookAtRig_grp_orientConstraint1.cro";
connectAttr "eye_lookAtRig_grp.pim" "eye_lookAtRig_grp_orientConstraint1.cpim";
connectAttr "eyeBall_input.r" "eye_lookAtRig_grp_orientConstraint1.tg[0].tr";
connectAttr "eyeBall_input.ro" "eye_lookAtRig_grp_orientConstraint1.tg[0].tro";
connectAttr "eyeBall_input.pm" "eye_lookAtRig_grp_orientConstraint1.tg[0].tpm";
connectAttr "eyeBall_input.jo" "eye_lookAtRig_grp_orientConstraint1.tg[0].tjo";
connectAttr "eye_lookAtRig_grp_orientConstraint1.w0" "eye_lookAtRig_grp_orientConstraint1.tg[0].tw"
		;
connectAttr "|eyeBall_grp|upperLid_zro.ro" "upperLid_zro_orientConstraint1.cro";
connectAttr "|eyeBall_grp|upperLid_zro.pim" "upperLid_zro_orientConstraint1.cpim"
		;
connectAttr "upperLid_input.r" "upperLid_zro_orientConstraint1.tg[0].tr";
connectAttr "upperLid_input.ro" "upperLid_zro_orientConstraint1.tg[0].tro";
connectAttr "upperLid_input.pm" "upperLid_zro_orientConstraint1.tg[0].tpm";
connectAttr "upperLid_input.jo" "upperLid_zro_orientConstraint1.tg[0].tjo";
connectAttr "upperLid_zro_orientConstraint1.w0" "upperLid_zro_orientConstraint1.tg[0].tw"
		;
connectAttr "|eyeBall_grp|lowerLid_zro.ro" "lowerLid_zro_orientConstraint1.cro";
connectAttr "|eyeBall_grp|lowerLid_zro.pim" "lowerLid_zro_orientConstraint1.cpim"
		;
connectAttr "lowerLid_input.r" "lowerLid_zro_orientConstraint1.tg[0].tr";
connectAttr "lowerLid_input.ro" "lowerLid_zro_orientConstraint1.tg[0].tro";
connectAttr "lowerLid_input.pm" "lowerLid_zro_orientConstraint1.tg[0].tpm";
connectAttr "lowerLid_input.jo" "lowerLid_zro_orientConstraint1.tg[0].tjo";
connectAttr "lowerLid_zro_orientConstraint1.w0" "lowerLid_zro_orientConstraint1.tg[0].tw"
		;
connectAttr "eyeLookAt_zro.pim" "eyeLookAt_zro_pointConstraint1.cpim";
connectAttr "eyeLookAt_zro.rp" "eyeLookAt_zro_pointConstraint1.crp";
connectAttr "eyeLookAt_zro.rpt" "eyeLookAt_zro_pointConstraint1.crt";
connectAttr "iris_input.t" "eyeLookAt_zro_pointConstraint1.tg[0].tt";
connectAttr "iris_input.rp" "eyeLookAt_zro_pointConstraint1.tg[0].trp";
connectAttr "iris_input.rpt" "eyeLookAt_zro_pointConstraint1.tg[0].trt";
connectAttr "iris_input.pm" "eyeLookAt_zro_pointConstraint1.tg[0].tpm";
connectAttr "eyeLookAt_zro_pointConstraint1.w0" "eyeLookAt_zro_pointConstraint1.tg[0].tw"
		;
connectAttr "null4.ro" "null4_orientConstraint1.cro";
connectAttr "null4.pim" "null4_orientConstraint1.cpim";
connectAttr "eyeBall_input.r" "null4_orientConstraint1.tg[0].tr";
connectAttr "eyeBall_input.ro" "null4_orientConstraint1.tg[0].tro";
connectAttr "eyeBall_input.pm" "null4_orientConstraint1.tg[0].tpm";
connectAttr "eyeBall_input.jo" "null4_orientConstraint1.tg[0].tjo";
connectAttr "null4_orientConstraint1.w0" "null4_orientConstraint1.tg[0].tw";
connectAttr "lowerLid_input.r" "null4_orientConstraint1.tg[1].tr";
connectAttr "lowerLid_input.ro" "null4_orientConstraint1.tg[1].tro";
connectAttr "lowerLid_input.pm" "null4_orientConstraint1.tg[1].tpm";
connectAttr "lowerLid_input.jo" "null4_orientConstraint1.tg[1].tjo";
connectAttr "null4_orientConstraint1.w1" "null4_orientConstraint1.tg[1].tw";
connectAttr "eye_output.s" "eyeBall_output.is";
connectAttr "eyeBall_L_jnt_orientConstraint1.crx" "eyeBall_output.rx";
connectAttr "eyeBall_L_jnt_orientConstraint1.cry" "eyeBall_output.ry";
connectAttr "eyeBall_L_jnt_orientConstraint1.crz" "eyeBall_output.rz";
connectAttr "eyeBall_output.s" "iris_output.is";
connectAttr "eyeBall_output.ro" "eyeBall_L_jnt_orientConstraint1.cro";
connectAttr "eyeBall_output.pim" "eyeBall_L_jnt_orientConstraint1.cpim";
connectAttr "eyeBall_output.jo" "eyeBall_L_jnt_orientConstraint1.cjo";
connectAttr "eyeBall_output.is" "eyeBall_L_jnt_orientConstraint1.is";
connectAttr "const_eyeJnt.r" "eyeBall_L_jnt_orientConstraint1.tg[0].tr";
connectAttr "const_eyeJnt.ro" "eyeBall_L_jnt_orientConstraint1.tg[0].tro";
connectAttr "const_eyeJnt.pm" "eyeBall_L_jnt_orientConstraint1.tg[0].tpm";
connectAttr "eyeBall_L_jnt_orientConstraint1.w0" "eyeBall_L_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "eye_output.s" "upperLid_output.is";
connectAttr "upperLid_L_jnt_orientConstraint1.crx" "upperLid_output.rx";
connectAttr "upperLid_L_jnt_orientConstraint1.cry" "upperLid_output.ry";
connectAttr "upperLid_L_jnt_orientConstraint1.crz" "upperLid_output.rz";
connectAttr "upperLid_output.s" "upperLidEnd_output.is";
connectAttr "upperLid_output.ro" "upperLid_L_jnt_orientConstraint1.cro";
connectAttr "upperLid_output.pim" "upperLid_L_jnt_orientConstraint1.cpim";
connectAttr "upperLid_output.jo" "upperLid_L_jnt_orientConstraint1.cjo";
connectAttr "upperLid_output.is" "upperLid_L_jnt_orientConstraint1.is";
connectAttr "upperLid_FK_ctrl.r" "upperLid_L_jnt_orientConstraint1.tg[0].tr";
connectAttr "upperLid_FK_ctrl.ro" "upperLid_L_jnt_orientConstraint1.tg[0].tro";
connectAttr "upperLid_FK_ctrl.pm" "upperLid_L_jnt_orientConstraint1.tg[0].tpm";
connectAttr "upperLid_L_jnt_orientConstraint1.w0" "upperLid_L_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "const_upperLidJnt.r" "upperLid_L_jnt_orientConstraint1.tg[1].tr";
connectAttr "const_upperLidJnt.ro" "upperLid_L_jnt_orientConstraint1.tg[1].tro";
connectAttr "const_upperLidJnt.pm" "upperLid_L_jnt_orientConstraint1.tg[1].tpm";
connectAttr "upperLid_L_jnt_orientConstraint1.w1" "upperLid_L_jnt_orientConstraint1.tg[1].tw"
		;
connectAttr "eye_output.s" "lowerLid_output.is";
connectAttr "lowerLid_L_jnt_orientConstraint1.crx" "lowerLid_output.rx";
connectAttr "lowerLid_L_jnt_orientConstraint1.cry" "lowerLid_output.ry";
connectAttr "lowerLid_L_jnt_orientConstraint1.crz" "lowerLid_output.rz";
connectAttr "lowerLid_output.s" "lowerLidEnd_output.is";
connectAttr "lowerLid_output.ro" "lowerLid_L_jnt_orientConstraint1.cro";
connectAttr "lowerLid_output.pim" "lowerLid_L_jnt_orientConstraint1.cpim";
connectAttr "lowerLid_output.jo" "lowerLid_L_jnt_orientConstraint1.cjo";
connectAttr "lowerLid_output.is" "lowerLid_L_jnt_orientConstraint1.is";
connectAttr "lowerLid_FK_ctrl.r" "lowerLid_L_jnt_orientConstraint1.tg[0].tr";
connectAttr "lowerLid_FK_ctrl.ro" "lowerLid_L_jnt_orientConstraint1.tg[0].tro";
connectAttr "lowerLid_FK_ctrl.pm" "lowerLid_L_jnt_orientConstraint1.tg[0].tpm";
connectAttr "lowerLid_L_jnt_orientConstraint1.w0" "lowerLid_L_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "const_lowerLidJnt.r" "lowerLid_L_jnt_orientConstraint1.tg[1].tr";
connectAttr "const_lowerLidJnt.ro" "lowerLid_L_jnt_orientConstraint1.tg[1].tro";
connectAttr "const_lowerLidJnt.pm" "lowerLid_L_jnt_orientConstraint1.tg[1].tpm";
connectAttr "lowerLid_L_jnt_orientConstraint1.w1" "lowerLid_L_jnt_orientConstraint1.tg[1].tw"
		;
connectAttr "eyeBall_grp_parentConstraint1.ctx" "eyeBall_grp.tx";
connectAttr "eyeBall_grp_parentConstraint1.cty" "eyeBall_grp.ty";
connectAttr "eyeBall_grp_parentConstraint1.ctz" "eyeBall_grp.tz";
connectAttr "eyeBall_grp_parentConstraint1.crx" "eyeBall_grp.rx";
connectAttr "eyeBall_grp_parentConstraint1.cry" "eyeBall_grp.ry";
connectAttr "eyeBall_grp_parentConstraint1.crz" "eyeBall_grp.rz";
connectAttr "eye_zro_orientConstraint1.crx" "|eyeBall_grp|eye_zro.rx";
connectAttr "eye_zro_orientConstraint1.cry" "|eyeBall_grp|eye_zro.ry";
connectAttr "eye_zro_orientConstraint1.crz" "|eyeBall_grp|eye_zro.rz";
connectAttr "lookAt_out.r" "eye_lookAt.r";
connectAttr "|eyeBall_grp|eye_zro.ro" "eye_zro_orientConstraint1.cro";
connectAttr "|eyeBall_grp|eye_zro.pim" "eye_zro_orientConstraint1.cpim";
connectAttr "eyeBall_input.r" "eye_zro_orientConstraint1.tg[0].tr";
connectAttr "eyeBall_input.ro" "eye_zro_orientConstraint1.tg[0].tro";
connectAttr "eyeBall_input.pm" "eye_zro_orientConstraint1.tg[0].tpm";
connectAttr "eyeBall_input.jo" "eye_zro_orientConstraint1.tg[0].tjo";
connectAttr "eye_zro_orientConstraint1.w0" "eye_zro_orientConstraint1.tg[0].tw";
connectAttr "upperLid_zro_orientConstraint1.crx" "|eyeBall_grp|upperLid_zro.rx";
connectAttr "upperLid_zro_orientConstraint1.cry" "|eyeBall_grp|upperLid_zro.ry";
connectAttr "upperLid_zro_orientConstraint1.crz" "|eyeBall_grp|upperLid_zro.rz";
connectAttr "upperLid_const.r" "upperLid_autoFollow.r";
connectAttr "upperLid_autoClose_orientConstraint1.crx" "upperLid_autoClose.rx";
connectAttr "upperLid_autoClose_orientConstraint1.cry" "upperLid_autoClose.ry";
connectAttr "upperLid_autoClose_orientConstraint1.crz" "upperLid_autoClose.rz";
connectAttr "upperLid_autoClose.ro" "upperLid_autoClose_orientConstraint1.cro";
connectAttr "upperLid_autoClose.pim" "upperLid_autoClose_orientConstraint1.cpim"
		;
connectAttr "upperLid_const_out.r" "upperLid_autoClose_orientConstraint1.tg[0].tr"
		;
connectAttr "upperLid_const_out.ro" "upperLid_autoClose_orientConstraint1.tg[0].tro"
		;
connectAttr "upperLid_const_out.pm" "upperLid_autoClose_orientConstraint1.tg[0].tpm"
		;
connectAttr "upperLid_autoClose_orientConstraint1.w0" "upperLid_autoClose_orientConstraint1.tg[0].tw"
		;
connectAttr "lowerLid_zro_orientConstraint1.crx" "|eyeBall_grp|lowerLid_zro.rx";
connectAttr "lowerLid_zro_orientConstraint1.cry" "|eyeBall_grp|lowerLid_zro.ry";
connectAttr "lowerLid_zro_orientConstraint1.crz" "|eyeBall_grp|lowerLid_zro.rz";
connectAttr "lowerLid_const.r" "lowerLid_autoFollow.r";
connectAttr "lowerLid_autoClose_orientConstraint1.crx" "lowerLid_autoClose.rx";
connectAttr "lowerLid_autoClose_orientConstraint1.cry" "lowerLid_autoClose.ry";
connectAttr "lowerLid_autoClose_orientConstraint1.crz" "lowerLid_autoClose.rz";
connectAttr "lowerLid_autoClose.ro" "lowerLid_autoClose_orientConstraint1.cro";
connectAttr "lowerLid_autoClose.pim" "lowerLid_autoClose_orientConstraint1.cpim"
		;
connectAttr "lowerLid_const_out.r" "lowerLid_autoClose_orientConstraint1.tg[0].tr"
		;
connectAttr "lowerLid_const_out.ro" "lowerLid_autoClose_orientConstraint1.tg[0].tro"
		;
connectAttr "lowerLid_const_out.pm" "lowerLid_autoClose_orientConstraint1.tg[0].tpm"
		;
connectAttr "lowerLid_autoClose_orientConstraint1.w0" "lowerLid_autoClose_orientConstraint1.tg[0].tw"
		;
connectAttr "eye_lookAtRig_grp_orientConstraint1.crx" "eye_lookAtRig_grp.rx";
connectAttr "eye_lookAtRig_grp_orientConstraint1.cry" "eye_lookAtRig_grp.ry";
connectAttr "eye_lookAtRig_grp_orientConstraint1.crz" "eye_lookAtRig_grp.rz";
connectAttr "null3_aimConstraint1.crx" "lookAt_out.rx";
connectAttr "null3_aimConstraint1.cry" "lookAt_out.ry";
connectAttr "null3_aimConstraint1.crz" "lookAt_out.rz";
connectAttr "lookAt_out.pim" "null3_aimConstraint1.cpim";
connectAttr "lookAt_out.t" "null3_aimConstraint1.ct";
connectAttr "lookAt_out.rp" "null3_aimConstraint1.crp";
connectAttr "lookAt_out.rpt" "null3_aimConstraint1.crt";
connectAttr "lookAt_out.ro" "null3_aimConstraint1.cro";
connectAttr "eyeLookAt__SIDE__ctrl.t" "null3_aimConstraint1.tg[0].tt";
connectAttr "eyeLookAt__SIDE__ctrl.rp" "null3_aimConstraint1.tg[0].trp";
connectAttr "eyeLookAt__SIDE__ctrl.rpt" "null3_aimConstraint1.tg[0].trt";
connectAttr "eyeLookAt__SIDE__ctrl.pm" "null3_aimConstraint1.tg[0].tpm";
connectAttr "null3_aimConstraint1.w0" "null3_aimConstraint1.tg[0].tw";
connectAttr "eyeLookAt_zro_pointConstraint1.ctx" "eyeLookAt_zro.tx";
connectAttr "eyeLookAt_zro_pointConstraint1.cty" "eyeLookAt_zro.ty";
connectAttr "eyeLookAt_zro_pointConstraint1.ctz" "eyeLookAt_zro.tz";
connectAttr "null4_orientConstraint1.crx" "null4.rx";
connectAttr "null4_orientConstraint1.cry" "null4.ry";
connectAttr "null4_orientConstraint1.crz" "null4.rz";
connectAttr "close_tgt_aimConstraint1.crx" "close_tgt_driver.rx";
connectAttr "close_tgt_aimConstraint1.cry" "close_tgt_driver.ry";
connectAttr "close_tgt_aimConstraint1.crz" "close_tgt_driver.rz";
connectAttr "close_tgt_driver.pim" "close_tgt_aimConstraint1.cpim";
connectAttr "close_tgt_driver.t" "close_tgt_aimConstraint1.ct";
connectAttr "close_tgt_driver.rp" "close_tgt_aimConstraint1.crp";
connectAttr "close_tgt_driver.rpt" "close_tgt_aimConstraint1.crt";
connectAttr "close_tgt_driver.ro" "close_tgt_aimConstraint1.cro";
connectAttr "eyeClose_ctrl.t" "close_tgt_aimConstraint1.tg[0].tt";
connectAttr "eyeClose_ctrl.rp" "close_tgt_aimConstraint1.tg[0].trp";
connectAttr "eyeClose_ctrl.rpt" "close_tgt_aimConstraint1.tg[0].trt";
connectAttr "eyeClose_ctrl.pm" "close_tgt_aimConstraint1.tg[0].tpm";
connectAttr "close_tgt_aimConstraint1.w0" "close_tgt_aimConstraint1.tg[0].tw";
connectAttr "upperLid_tgt_orientConstraint1.crx" "consted_lowerLid_autoFollow.rx"
		;
connectAttr "upperLid_tgt_orientConstraint1.cry" "consted_lowerLid_autoFollow.ry"
		;
connectAttr "upperLid_tgt_orientConstraint1.crz" "consted_lowerLid_autoFollow.rz"
		;
connectAttr "consted_lowerLid_autoFollow.ro" "upperLid_tgt_orientConstraint1.cro"
		;
connectAttr "consted_lowerLid_autoFollow.pim" "upperLid_tgt_orientConstraint1.cpim"
		;
connectAttr "upperLid_autoFollow.r" "upperLid_tgt_orientConstraint1.tg[0].tr";
connectAttr "upperLid_autoFollow.ro" "upperLid_tgt_orientConstraint1.tg[0].tro";
connectAttr "upperLid_autoFollow.pm" "upperLid_tgt_orientConstraint1.tg[0].tpm";
connectAttr "upperLid_tgt_orientConstraint1.w0" "upperLid_tgt_orientConstraint1.tg[0].tw"
		;
connectAttr "lowerLid_tgt_orientConstraint1.crx" "consted_upperLid_autoFollow.rx"
		;
connectAttr "lowerLid_tgt_orientConstraint1.cry" "consted_upperLid_autoFollow.ry"
		;
connectAttr "lowerLid_tgt_orientConstraint1.crz" "consted_upperLid_autoFollow.rz"
		;
connectAttr "consted_upperLid_autoFollow.ro" "lowerLid_tgt_orientConstraint1.cro"
		;
connectAttr "consted_upperLid_autoFollow.pim" "lowerLid_tgt_orientConstraint1.cpim"
		;
connectAttr "lowerLid_autoFollow.r" "lowerLid_tgt_orientConstraint1.tg[0].tr";
connectAttr "lowerLid_autoFollow.ro" "lowerLid_tgt_orientConstraint1.tg[0].tro";
connectAttr "lowerLid_autoFollow.pm" "lowerLid_tgt_orientConstraint1.tg[0].tpm";
connectAttr "lowerLid_tgt_orientConstraint1.w0" "lowerLid_tgt_orientConstraint1.tg[0].tw"
		;
connectAttr "upperLid_const_orientConstraint1.crx" "upperLid_const_out.rx";
connectAttr "upperLid_const_orientConstraint1.cry" "upperLid_const_out.ry";
connectAttr "upperLid_const_orientConstraint1.crz" "upperLid_const_out.rz";
connectAttr "upperLid_const_out.ro" "upperLid_const_orientConstraint1.cro";
connectAttr "upperLid_const_out.pim" "upperLid_const_orientConstraint1.cpim";
connectAttr "close_tgt_driver.r" "upperLid_const_orientConstraint1.tg[0].tr";
connectAttr "close_tgt_driver.ro" "upperLid_const_orientConstraint1.tg[0].tro";
connectAttr "close_tgt_driver.pm" "upperLid_const_orientConstraint1.tg[0].tpm";
connectAttr "upperLid_const_orientConstraint1.w0" "upperLid_const_orientConstraint1.tg[0].tw"
		;
connectAttr "consted_lowerLid_autoFollow.r" "upperLid_const_orientConstraint1.tg[1].tr"
		;
connectAttr "consted_lowerLid_autoFollow.ro" "upperLid_const_orientConstraint1.tg[1].tro"
		;
connectAttr "consted_lowerLid_autoFollow.pm" "upperLid_const_orientConstraint1.tg[1].tpm"
		;
connectAttr "upperLid_const_orientConstraint1.w1" "upperLid_const_orientConstraint1.tg[1].tw"
		;
connectAttr "eyeClose_ctrl.close" "upperLid_const_orientConstraint1.w0";
connectAttr "upperLid_const_orientConstraint1_upperLid_tgtW1.o" "upperLid_const_orientConstraint1.w1"
		;
connectAttr "lowerLid_const_orientConstraint1.crx" "lowerLid_const_out.rx";
connectAttr "lowerLid_const_orientConstraint1.cry" "lowerLid_const_out.ry";
connectAttr "lowerLid_const_orientConstraint1.crz" "lowerLid_const_out.rz";
connectAttr "lowerLid_const_out.ro" "lowerLid_const_orientConstraint1.cro";
connectAttr "lowerLid_const_out.pim" "lowerLid_const_orientConstraint1.cpim";
connectAttr "close_tgt_driver.r" "lowerLid_const_orientConstraint1.tg[0].tr";
connectAttr "close_tgt_driver.ro" "lowerLid_const_orientConstraint1.tg[0].tro";
connectAttr "close_tgt_driver.pm" "lowerLid_const_orientConstraint1.tg[0].tpm";
connectAttr "lowerLid_const_orientConstraint1.w0" "lowerLid_const_orientConstraint1.tg[0].tw"
		;
connectAttr "consted_upperLid_autoFollow.r" "lowerLid_const_orientConstraint1.tg[1].tr"
		;
connectAttr "consted_upperLid_autoFollow.ro" "lowerLid_const_orientConstraint1.tg[1].tro"
		;
connectAttr "consted_upperLid_autoFollow.pm" "lowerLid_const_orientConstraint1.tg[1].tpm"
		;
connectAttr "lowerLid_const_orientConstraint1.w1" "lowerLid_const_orientConstraint1.tg[1].tw"
		;
connectAttr "eyeClose_ctrl.close" "lowerLid_const_orientConstraint1.w0";
connectAttr "lowerLid_const_orientConstraint1_lowerLid_tgtW1.o" "lowerLid_const_orientConstraint1.w1"
		;
connectAttr "|eyeBall_grp|eye_zro.r" "|eyeBall_grp|lid_autoFollowRig_grp|eye_zro.r"
		;
connectAttr "eye_rotation_orientConstraint1.crx" "eye_rotation.rx";
connectAttr "eye_rotation_orientConstraint1.cry" "eye_rotation.ry";
connectAttr "eye_rotation_orientConstraint1.crz" "eye_rotation.rz";
connectAttr "eye_rotation.ro" "eye_rotation_orientConstraint1.cro";
connectAttr "eye_rotation.pim" "eye_rotation_orientConstraint1.cpim";
connectAttr "const_eyeJnt.r" "eye_rotation_orientConstraint1.tg[0].tr";
connectAttr "const_eyeJnt.ro" "eye_rotation_orientConstraint1.tg[0].tro";
connectAttr "const_eyeJnt.pm" "eye_rotation_orientConstraint1.tg[0].tpm";
connectAttr "eye_rotation_orientConstraint1.w0" "eye_rotation_orientConstraint1.tg[0].tw"
		;
connectAttr "upperLid_const_orientConstraint2.crz" "upperLid_const.rz";
connectAttr "upperLid_autoFollow_max.rz" "upperLid_const.xrzl";
connectAttr "upperLid_autoFollow_min.rz" "upperLid_const.mrzl";
connectAttr "upperLid_const.ro" "upperLid_const_orientConstraint2.cro";
connectAttr "upperLid_const.pim" "upperLid_const_orientConstraint2.cpim";
connectAttr "eye_rotation.r" "upperLid_const_orientConstraint2.tg[0].tr";
connectAttr "eye_rotation.ro" "upperLid_const_orientConstraint2.tg[0].tro";
connectAttr "eye_rotation.pm" "upperLid_const_orientConstraint2.tg[0].tpm";
connectAttr "upperLid_const_orientConstraint2.w0" "upperLid_const_orientConstraint2.tg[0].tw"
		;
connectAttr "|eyeBall_grp|lid_autoFollowRig_grp|eye_zro.r" "upperLid_const_orientConstraint2.tg[1].tr"
		;
connectAttr "|eyeBall_grp|lid_autoFollowRig_grp|eye_zro.ro" "upperLid_const_orientConstraint2.tg[1].tro"
		;
connectAttr "|eyeBall_grp|lid_autoFollowRig_grp|eye_zro.pm" "upperLid_const_orientConstraint2.tg[1].tpm"
		;
connectAttr "upperLid_const_orientConstraint2.w1" "upperLid_const_orientConstraint2.tg[1].tw"
		;
connectAttr "upperLid_const_orientConstraint2_eye_zroW1.o" "upperLid_const_orientConstraint2.w1"
		;
connectAttr "lowerLid_const_orientConstraint2.crz" "lowerLid_const.rz";
connectAttr "lowerLid_autoFollow_max.rz" "lowerLid_const.xrzl";
connectAttr "lowerLid_autoFollow_min.rz" "lowerLid_const.mrzl";
connectAttr "lowerLid_const.ro" "lowerLid_const_orientConstraint2.cro";
connectAttr "lowerLid_const.pim" "lowerLid_const_orientConstraint2.cpim";
connectAttr "eye_rotation.r" "lowerLid_const_orientConstraint2.tg[0].tr";
connectAttr "eye_rotation.ro" "lowerLid_const_orientConstraint2.tg[0].tro";
connectAttr "eye_rotation.pm" "lowerLid_const_orientConstraint2.tg[0].tpm";
connectAttr "lowerLid_const_orientConstraint2.w0" "lowerLid_const_orientConstraint2.tg[0].tw"
		;
connectAttr "|eyeBall_grp|lid_autoFollowRig_grp|eye_zro.r" "lowerLid_const_orientConstraint2.tg[1].tr"
		;
connectAttr "|eyeBall_grp|lid_autoFollowRig_grp|eye_zro.ro" "lowerLid_const_orientConstraint2.tg[1].tro"
		;
connectAttr "|eyeBall_grp|lid_autoFollowRig_grp|eye_zro.pm" "lowerLid_const_orientConstraint2.tg[1].tpm"
		;
connectAttr "lowerLid_const_orientConstraint2.w1" "lowerLid_const_orientConstraint2.tg[1].tw"
		;
connectAttr "lowerLid_const_orientConstraint2_eye_zroW1.o" "lowerLid_const_orientConstraint2.w1"
		;
connectAttr "|eyeBall_grp|upperLid_zro.r" "|eyeBall_grp|lid_autoFollowRig_grp|upperLid_zro.r"
		;
connectAttr "upperLid_const.r" "curve1.r";
connectAttr "|eyeBall_grp|lowerLid_zro.r" "|eyeBall_grp|lid_autoFollowRig_grp|lowerLid_zro.r"
		;
connectAttr "lowerLid_const.r" "curve2.r";
connectAttr "detachCurve1.oc[0]" "nurbsCircleShape1.cr";
connectAttr "detachCurve1.oc[1]" "detachedCurveShape1.cr";
connectAttr "detachCurve1.oc[2]" "detachedCurveShape2.cr";
connectAttr "detachCurve1.oc[3]" "detachedCurveShape3.cr";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "upperLid_const_orientConstraint1.w0" "upperLid_const_orientConstraint1_upperLid_tgtW1.i"
		;
connectAttr "lowerLid_const_orientConstraint1.w0" "lowerLid_const_orientConstraint1_lowerLid_tgtW1.i"
		;
connectAttr "lowerLid_const.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn";
connectAttr "upperLid_const.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn";
connectAttr "eye_rotation.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn";
connectAttr "upperLid_const_orientConstraint2.w0" "upperLid_const_orientConstraint2_eye_zroW1.i"
		;
connectAttr "lowerLid_const_orientConstraint2.w0" "lowerLid_const_orientConstraint2_eye_zroW1.i"
		;
connectAttr "layerManager.dli[1]" "layer1.id";
connectAttr "makeNurbCircle1.oc" "detachCurve1.ic";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of eye_rig.ma
