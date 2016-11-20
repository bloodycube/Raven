//Maya ASCII 2017 scene
//Name: eye_rig.ma
//Last modified: Sun, Nov 20, 2016 05:49:05 PM
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
createNode transform -n "module_grp";
	rename -uid "80BDD328-4D06-95DA-CD4B-69ACD779C245";
createNode transform -n "eyeBall_zro" -p "module_grp";
	rename -uid "65DF5A23-41D1-88EF-25DD-06BC99AE1961";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "eyeBall_lookAt" -p "eyeBall_zro";
	rename -uid "804EA34D-43D7-BABA-2E10-D8AB053AE747";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0.47399998 ;
createNode transform -n "eyeBall_FK_ctrl" -p "eyeBall_lookAt";
	rename -uid "FC1A1349-482E-948A-0346-F1AB14C171D6";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "eyeBall_FK_ctrlShape" -p "eyeBall_FK_ctrl";
	rename -uid "246BDB45-4514-6A89-2E42-BFBD0E160E7C";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".tw" yes;
createNode nurbsCurve -n "eyeBall_FK_ctrlShapeOrig" -p "eyeBall_FK_ctrl";
	rename -uid "1C1EB82B-4892-9193-3A29-54928B6E8EED";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.0000000000000016 0.78361162489122504 -0.78361162489122427
		0.99999999999999845 -2.652095841564378e-016 -1.1081941875543861
		1.0000000000000002 -0.78361162489122438 -0.78361162489122516
		0.99999999999999922 -1.1081941875543879 -3.2112695072372304e-016
		0.99999999999999989 -0.7836116248912246 0.7836116248912236
		0.99999999999999956 -4.449428388215676e-016 1.1081941875543877
		1.0000000000000013 0.78361162489122371 0.78361162489122416
		1.0000000000000016 1.1081941875543879 -5.1500976469709802e-016
		1.0000000000000016 0.78361162489122504 -0.78361162489122427
		0.99999999999999845 -2.652095841564378e-016 -1.1081941875543861
		1.0000000000000002 -0.78361162489122438 -0.78361162489122516
		;
createNode transform -n "eyeBall_constrainJnt" -p "eyeBall_FK_ctrl";
	rename -uid "6C188C9D-4B1F-4673-406E-49A543EC2C4D";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".hio" yes;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode transform -n "upperLid_zro" -p "module_grp";
	rename -uid "49488C88-41C3-7436-50E8-848B0372842B";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".s" -type "double3" 0.99999999999999956 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "upperLid_autoFollow" -p "upperLid_zro";
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
createNode transform -n "upperLid_FK_ctrl" -p "upperLid_autoClose";
	rename -uid "0CDA82B5-4F3B-CE16-81D3-D2B9709176F4";
	addAttr -ci true -sn "autoFollow_weight" -ln "autoFollow_weight" -dv 0.5 -min 0 
		-max 1 -at "double";
	addAttr -ci true -sn "autoFollow_max" -ln "autoFollow_max" -at "double";
	addAttr -ci true -sn "autoFollow_min" -ln "autoFollow_min" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".s" -type "double3" 0.99999999999999944 0.99999999999999967 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".autoFollow_weight" 0.7;
	setAttr -k on ".autoFollow_max" 10;
	setAttr -k on ".autoFollow_min" -38.1;
createNode nurbsCurve -n "upperLid_FK_ctrlShape" -p "upperLid_FK_ctrl";
	rename -uid "B5D5169B-4633-2EF5-14EC-9A83FD106675";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".tw" yes;
createNode nurbsCurve -n "upperLid_FK_ctrlShapeOrig" -p "upperLid_FK_ctrl";
	rename -uid "F5EE441C-4EE7-2CEA-7E8F-4CBB9C56A7F0";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 7 0 no 3
		12 0.25 0.25 0.25 0.75 0.75 0.75 1.75 2.75 3.75 4.75 4.75 4.75
		10
		0.99999999999999978 0 1
		1 0 0.33333333333333331
		1.0000000000000002 0 -0.33333333333333354
		1.0000000000000004 0 -1.0000000000000002
		1.0000000000000007 0.26120387496374164 -0.99999999999999922
		1.0000000000000004 0.78361162489122416 -0.78361162489122349
		1.0000000000000004 1.1081941875543875 2.4606854055572997e-016
		0.99999999999999989 0.78361162489122393 0.7836116248912236
		0.99999999999999978 0.26120387496374142 0.99999999999999922
		0.99999999999999967 -2.7755575615628901e-017 0.99999999999999911
		;
createNode transform -n "upperLid_constrainJnt" -p "upperLid_FK_ctrl";
	rename -uid "05CBF418-49FC-2AD0-1869-80AAE82B625C";
	setAttr ".s" -type "double3" 1.0000000000000002 0.99999999999999989 0.99999999999999956 ;
	setAttr ".hio" yes;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode transform -n "lowerLid_zro" -p "module_grp";
	rename -uid "2F14F88A-43E1-C41F-E141-58AF537B6BCE";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".s" -type "double3" 0.99999999999999956 0.99999999999999967 0.99999999999999956 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "lowerLid_autoFollow" -p "lowerLid_zro";
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
createNode transform -n "lowerLid_FK_ctrl" -p "lowerLid_autoClose";
	rename -uid "3B69DC12-4FE5-BE68-3F76-AC8299D276AA";
	addAttr -ci true -sn "autoFollow_weight" -ln "autoFollow_weight" -min 0 -max 1 
		-at "double";
	addAttr -ci true -sn "autoFollow_max" -ln "autoFollow_max" -at "double";
	addAttr -ci true -sn "autoFollow_min" -ln "autoFollow_min" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".s" -type "double3" 0.99999999999999911 0.99999999999999944 0.99999999999999944 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".autoFollow_weight" 0.3;
	setAttr -k on ".autoFollow_max" 10;
	setAttr -k on ".autoFollow_min" -10;
createNode nurbsCurve -n "lowerLid_FK_ctrlShape" -p "lowerLid_FK_ctrl";
	rename -uid "6082D34C-483A-5F3A-54D1-8980C1BFAAA8";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".tw" yes;
createNode nurbsCurve -n "lowerLid_FK_ctrlShapeOrig" -p "lowerLid_FK_ctrl";
	rename -uid "DE88E698-41C2-0F10-D27D-3DB4E681D13B";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 7 0 no 3
		12 0.25 0.25 0.25 0.75 0.75 0.75 1.75 2.75 3.75 4.75 4.75 4.75
		10
		1.0000000000000002 0 0.99999999999999978
		1.0000000000000004 0 0.33333333333333298
		1.0000000000000007 0 -0.33333333333333343
		1.0000000000000009 0 -1.0000000000000007
		1.0000000000000009 -0.26120387496374103 -0.99999999999999978
		1.0000000000000007 -0.78361162489122382 -0.78361162489122427
		1.0000000000000002 -1.1081941875543877 -9.122023553308231e-016
		1 -0.78361162489122504 0.78361162489122282
		1.0000000000000002 -0.26120387496374153 0.99999999999999878
		1.0000000000000002 -2.775557561562891e-017 0.99999999999999878
		;
createNode transform -n "lowerLid_constrainJnt" -p "lowerLid_FK_ctrl";
	rename -uid "F4667C45-4A9E-7779-49E1-209B21A69CC1";
	setAttr ".s" -type "double3" 1.0000000000000004 1.0000000000000002 0.99999999999999978 ;
	setAttr ".hio" yes;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode transform -n "lookAt_zro" -p "module_grp";
	rename -uid "74D00D1D-4898-0400-7B08-3D88ABF39D78";
	setAttr ".t" -type "double3" 9.9999999999999964 0 -4.8985871965894059e-016 ;
	setAttr -av ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "lookAt_ctrl" -p "lookAt_zro";
	rename -uid "6F493AEA-404C-879F-237D-08A0B5D45232";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "lookAt_ctrlShape" -p "lookAt_ctrl";
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
createNode transform -n "autoLidClose_zro" -p "module_grp";
	rename -uid "05067754-4EC0-FA22-3E1F-DEB33B1A18AE";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999967 0.99999999999999989 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "autoClose_ctrl" -p "autoLidClose_zro";
	rename -uid "A0C7F950-4D38-4D7B-9ABC-7A9ACF0B083C";
	addAttr -ci true -sn "close" -ln "close" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 0 0 -14.999999999999998 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".close";
createNode nurbsCurve -n "autoClose_ctrlShape" -p "autoClose_ctrl";
	rename -uid "ED19110F-4577-2262-1CA2-ADA11BD3A8CD";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".tw" yes;
createNode nurbsCurve -n "autoClose_ctrlShapeOrig" -p "autoClose_ctrl";
	rename -uid "C4F91BDD-45BB-50CA-090F-C8996DEB5D50";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 15 0 no 3
		20 5.6877797689999987 5.6877797689999987 5.6877797689999987 6.0000163859999986
		 6.3122366169999991 6.3122366169999991 6.3122366169999991 6.388233862499999 6.388233862499999
		 6.388233862499999 6.7004540934999994 7.0126907104999994 7.0126907104999994 7.0126907104999994
		 7.0886918676999997 7.0886918676999997 7.0886918676999997 7.1646930247 7.1646930247
		 7.1646930247
		18
		1.163184637675988 1.7807104044977043e-017 -0.29081207834577349
		1.1873423570216504 1.1985483159306487e-017 -0.19573779423832646
		1.2126569787124486 3.1449566823265004e-022 -5.1361040334596547e-006
		1.1873436855185926 -1.1984854167970021e-017 0.19572752203025945
		1.163188440931068 -1.7806187497508441e-017 0.29079710998968528
		1.0985668608255774 0 0.27464171520639435
		1.033945280777014 0 0.25848632019425349
		0.96932370072845053 0 0.24233092518211263
		0.98945307126549398 -9.9873784733083507e-018 0.16310626835854958
		1.0105474822603737 2.6207972352720834e-022 -4.2800866945497118e-006
		0.98945196418470871 9.9879026327554051e-018 -0.1631148285319387
		0.96932053139665664 1.4839253370814204e-017 -0.24234339862147794
		1.0339419002982468 0 -0.25849962483556571
		1.0985632690828298 0 -0.2746558513917744
		1.1631846378674124 0 -0.29081207794798308
		1.0985632689978029 0 -0.27465585137051657
		1.0339419003832733 0 -0.25849962485682354
		0.969320531768744 0 -0.24234339834313057
		;
createNode transform -n "lid_autoClose_rotation" -p "autoClose_ctrl";
	rename -uid "F77FC0A1-441D-D8C7-04F7-D199CB08E1EB";
	setAttr ".s" -type "double3" 1.0000000000000007 1.0000000000000002 1 ;
	setAttr ".hio" yes;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode transform -n "rig_grp" -p "module_grp";
	rename -uid "13F93C55-4CE9-FBB3-CB9A-59AA4C77C6E8";
	setAttr ".v" no;
	setAttr ".hio" yes;
createNode transform -n "lookAtRig_grp" -p "rig_grp";
	rename -uid "E467E2C9-4DDF-BFDA-BCD9-879925A1AFFE";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0.47399998 ;
createNode transform -n "lookAt_result" -p "lookAtRig_grp";
	rename -uid "7ABA3D83-4F93-52F2-BD4F-9FA65C9213ED";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode aimConstraint -n "eye_lookAt_result_aimConstraint1" -p "lookAt_result";
	rename -uid "76431D4B-406E-59E9-34D6-739DA93A0CCE";
	addAttr -dcb 0 -ci true -sn "w0" -ln "eye_lookAt_ctrlW0" -dv 1 -at "double";
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
	setAttr ".wut" 2;
	setAttr ".rsrr" -type "double3" -1.6956148979193959 13.196563936060571 -7.3883226741997463 ;
	setAttr -k on ".w0";
createNode transform -n "autoLidFollowRig_grp" -p "rig_grp";
	rename -uid "DA8991E1-4ED1-5C10-9D61-47A09CF7F216";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "eye_rotation_zro" -p "autoLidFollowRig_grp";
	rename -uid "A909D761-48E5-BA29-74CB-BA98DB356F8B";
createNode transform -n "eye_rotation" -p "eye_rotation_zro";
	rename -uid "88DEBBC1-4777-9671-50D6-FDB6E946D553";
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1 ;
createNode orientConstraint -n "eye_rotation_orientConstraint1" -p "eye_rotation";
	rename -uid "41CF7C7E-49FD-4983-9061-519824C02052";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "constrainJnt_eyeW0" -dv 1 -min 0 
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
	setAttr ".int" 2;
	setAttr -k on ".w0";
createNode transform -n "upperLid_autoFollow_result" -p "eye_rotation_zro";
	rename -uid "EBE1A7DF-4DA8-44F2-373E-3D89493AF721";
	setAttr ".s" -type "double3" 0.99999999999999978 1 1 ;
	setAttr ".mnrl" -type "double3" 0 0 -38.1 ;
	setAttr ".mxrl" -type "double3" 0 0 10 ;
	setAttr ".mrxe" yes;
	setAttr ".mrye" yes;
	setAttr ".mrze" yes;
	setAttr ".xrxe" yes;
	setAttr ".xrye" yes;
	setAttr ".xrze" yes;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode orientConstraint -n "upperLid_autoFollow_result_orientConstraint1" -p "upperLid_autoFollow_result";
	rename -uid "71689D21-4160-EF0D-A23B-BB95A71E918A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "eye_rotationW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "eye_rotation_zroW1" -dv 1 -min 0 -at "double";
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
	setAttr ".int" 2;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "lowerLid_autoFollow_result" -p "eye_rotation_zro";
	rename -uid "F6E2B433-42A1-670E-812F-949CB3481B09";
	setAttr ".mnrl" -type "double3" 0 0 -10 ;
	setAttr ".mxrl" -type "double3" 0 0 10 ;
	setAttr ".mrxe" yes;
	setAttr ".mrye" yes;
	setAttr ".mrze" yes;
	setAttr ".xrxe" yes;
	setAttr ".xrye" yes;
	setAttr ".xrze" yes;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode orientConstraint -n "lowerLid_autoFollow_result_orientConstraint1" -p "lowerLid_autoFollow_result";
	rename -uid "7C6B89D7-41F3-5D87-7D0C-118D8CFDC86F";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "eye_rotationW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "eye_rotation_zroW1" -dv 1 -min 0 -at "double";
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
	setAttr ".int" 2;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "upperLid_rotation_zro" -p "autoLidFollowRig_grp";
	rename -uid "368E7BB1-48DF-5C9C-471C-8687394FFF9E";
createNode transform -n "upperLid_maxRotation" -p "upperLid_rotation_zro";
	rename -uid "88665D6B-498E-0B21-D71F-DD9AEA76E204";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr ".s" -type "double3" 0.99999999999999989 1 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "upperLid_maxRotationShape" -p "upperLid_maxRotation";
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
createNode transform -n "upperLid_minRotation" -p "upperLid_rotation_zro";
	rename -uid "EFE425D0-4074-037A-867D-F089A0107546";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr ".s" -type "double3" 0.99999999999999989 1.0000000000000002 1.0000000000000002 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "upperLid_minRotationShape" -p "upperLid_minRotation";
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
createNode transform -n "upperLid_rotation" -p "upperLid_rotation_zro";
	rename -uid "9F8BD3EF-4FCE-6AC4-FEA7-C698A6BB9E19";
createNode nurbsCurve -n "upperLid_rotationShape" -p "upperLid_rotation";
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
createNode transform -n "lowerLid_rotation_zro" -p "autoLidFollowRig_grp";
	rename -uid "2FC67DC9-4C77-05C9-CA83-93B94925543A";
createNode transform -n "lowerLid_maxRotation" -p "lowerLid_rotation_zro";
	rename -uid "CECE6055-49D0-30A8-E7E6-8184FC7123DC";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "lowerLid_maxRotationShape" -p "lowerLid_maxRotation";
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
createNode transform -n "lowerLid_minRotation" -p "lowerLid_rotation_zro";
	rename -uid "F1FB623A-413B-4B6A-85F7-0EAC369708BC";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "lowerLid_minRotationShape" -p "lowerLid_minRotation";
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
createNode transform -n "lowerLid_rotation" -p "lowerLid_rotation_zro";
	rename -uid "BA595654-4454-E317-E5A2-6DBDD90CE5C5";
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
createNode nurbsCurve -n "lowerLid_rotationShape" -p "lowerLid_rotation";
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
createNode transform -n "autoLidCloseRig_grp" -p "rig_grp";
	rename -uid "47D960F7-4904-5D81-9AC4-4B85B79C5B6D";
	addAttr -ci true -sn "close" -ln "close" -min 0 -max 1 -at "double";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 1 1 ;
	setAttr -k on ".close";
createNode transform -n "upperLid_autoFollow_rotation" -p "autoLidCloseRig_grp";
	rename -uid "A513759A-4A3D-9124-0AD5-DD971069C906";
createNode orientConstraint -n "upperLid_autoFollow_rotation_orientConstraint1" 
		-p "upperLid_autoFollow_rotation";
	rename -uid "75BF51F7-4519-27FC-C4D6-0185AEBF93D3";
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
	setAttr ".lr" -type "double3" 0 0 9.9999999999999982 ;
	setAttr ".rsrr" -type "double3" 0 0 18.882853277886181 ;
	setAttr ".int" 2;
	setAttr -k on ".w0";
createNode transform -n "lowerLid_autoFollow_rotation" -p "autoLidCloseRig_grp";
	rename -uid "6EFF8C7F-45C0-853E-C0E5-608849985558";
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999989 1 ;
createNode orientConstraint -n "lowerLid_autoFollow_rotation_orientConstraint1" -p
		 "lowerLid_autoFollow_rotation";
	rename -uid "C1667FA3-4C4B-3989-5B4C-3D848E267679";
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
	setAttr ".rsrr" -type "double3" 0 0 -20.797961953879454 ;
	setAttr ".int" 2;
	setAttr -k on ".w0";
createNode transform -n "upperLid_autoClose_result" -p "autoLidCloseRig_grp";
	rename -uid "065289CE-458B-8296-EB22-EDBEE4900056";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode orientConstraint -n "upperLid_autoClose_result_orientConstraint1" -p "upperLid_autoClose_result";
	rename -uid "A4A54E34-4248-53AD-1469-2EAB0DD0BA9A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "close_rotationW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "upperLid_autoFollow_rotationW1" -dv 
		1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 0 0 9.9999999999999982 ;
	setAttr ".rsrr" -type "double3" 5.5324431118451649 44.866240159913012 13.350410166041017 ;
	setAttr ".int" 2;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "lowerLid_autoClose_result" -p "autoLidCloseRig_grp";
	rename -uid "42A45A22-46F3-C982-A34E-329E5F6E7555";
	setAttr ".s" -type "double3" 1.0000000000000002 1 1 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode orientConstraint -n "lowerLid_autoClose_result_orientConstraint1" -p "lowerLid_autoClose_result";
	rename -uid "42B7885E-4611-AF0C-0739-D392DCAFAD15";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "close_rotationW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "lowerLid_autoFollow_rotationW1" -dv 
		1 -min 0 -at "double";
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
	setAttr ".rsrr" -type "double3" -6.0939663036847609 44.837656213682962 -14.703995650194686 ;
	setAttr ".int" 2;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "clst_grp" -p "rig_grp";
	rename -uid "A9A1666D-4C58-805E-4DCF-F6A0DF04C0CE";
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
createNode transform -n "clst_eyeZro_grp" -p "clst_grp";
	rename -uid "1173AFAB-4704-9DA7-80E2-788917D480AE";
	setAttr ".s" -type "double3" 0.99999999999999989 1 1 ;
createNode transform -n "cluster3Handle" -p "clst_eyeZro_grp";
	rename -uid "BFD70EA1-4C45-134F-132E-E088D28692F4";
createNode clusterHandle -n "cluster3HandleShape" -p "cluster3Handle";
	rename -uid "62C0CBFD-4373-A378-1A13-D5BB4D632953";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 0 7.7715611723760958e-016 ;
createNode transform -n "clst_upperLidZro_grp" -p "clst_grp";
	rename -uid "BFCF5EAC-4511-39FC-DFD9-29B712B6E9D8";
	setAttr ".s" -type "double3" 0.99999999999999989 1 1 ;
createNode transform -n "cluster1Handle" -p "clst_upperLidZro_grp";
	rename -uid "09D69FC3-43CC-9305-8625-78A7095FB751";
createNode clusterHandle -n "cluster1HandleShape" -p "cluster1Handle";
	rename -uid "7CDFA7FA-404B-32F1-C323-D8AAB983BBB6";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 0 -1.1102230246251565e-016 ;
createNode transform -n "clst_lowerLidZro_grp" -p "clst_grp";
	rename -uid "94409BC8-4236-06FC-F639-CDA9C07398FA";
createNode transform -n "cluster2Handle" -p "clst_lowerLidZro_grp";
	rename -uid "3EFFF04F-4EEB-A56F-13B2-CEAE280A1200";
createNode clusterHandle -n "cluster2HandleShape" -p "cluster2Handle";
	rename -uid "48127E75-45FD-BBA4-E0C7-44BD9A44A7D3";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
createNode transform -n "clst_closeZro_grp" -p "clst_grp";
	rename -uid "BA014F26-46A1-F0D7-D4ED-C8906520C9FC";
createNode transform -n "cluster4Handle" -p "clst_closeZro_grp";
	rename -uid "EEDD43C5-40F6-E68E-385C-AA9932101046";
createNode clusterHandle -n "cluster4HandleShape" -p "cluster4Handle";
	rename -uid "1D4EE3CA-428F-EBC8-19A0-1EB148E27CE8";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
createNode transform -n "input_grp" -p "rig_grp";
	rename -uid "D10C10E2-4493-549A-AA5B-E48D522C4E0B";
	setAttr ".s" -type "double3" 0.99999999999999956 1 0.99999999999999956 ;
	setAttr ".it" no;
createNode joint -n "input_eye" -p "input_grp";
	rename -uid "64FF8D81-4A4A-3809-FBA7-548F8B7AF2A1";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -89.999999999999986 0 ;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode joint -n "input_eyeBall" -p "input_eye";
	rename -uid "0B733D7B-41EF-B2AE-89D8-33A8AAB4871F";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eyeBall";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode joint -n "input_iris" -p "input_eyeBall";
	rename -uid "A2B1B249-4864-7AD6-A81B-6C982A5D581A";
	setAttr ".t" -type "double3" 4.9999999999999991 0 -4.8985871965894138e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "iris";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode joint -n "input_upperLid" -p "input_eye";
	rename -uid "AF1E8190-428F-3522-5CC1-94B13FF47130";
	setAttr ".r" -type "double3" 0 0 -3.180554681463516e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 10 ;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "upperLid";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode joint -n "input_upperLidEnd" -p "input_upperLid";
	rename -uid "CB45EBF8-47BC-DE3A-AF8A-49BDBD7DD6B5";
	setAttr ".t" -type "double3" 5 1.7763568394002493e-015 -3.2984547461676496e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "upperLidEnd";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode joint -n "input_lowerLid" -p "input_eye";
	rename -uid "56C5D7E3-4D15-4ADF-B05A-79A7AF5DB284";
	setAttr ".r" -type "double3" 0 0 3.180554681463516e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -20 ;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "lowerLid";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode joint -n "input_lowerLidEnd" -p "input_lowerLid";
	rename -uid "1060320D-462A-56F5-80B1-1BB70D491B1B";
	setAttr ".t" -type "double3" 5 -6.6613381477509392e-016 -4.8985871965894118e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr -k on ".jox";
	setAttr -k on ".joy";
	setAttr -k on ".joz";
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "lowerLidEnd";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "input_constGrp" -p "input_eye";
	rename -uid "76187485-428C-CA3B-1B35-678A2C5E644E";
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode parentConstraint -n "eyeBall_grp_parentConstraint1" -p "input_constGrp";
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
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "eye_lookAtRig_grp_orientConstraint1" -p "input_constGrp";
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
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "eye_zro_orientConstraint1" -p "input_constGrp";
	rename -uid "26568389-4CA3-1053-1BFD-07B32CE439CB";
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
	setAttr ".int" 2;
	setAttr -k on ".w0";
createNode orientConstraint -n "upperLid_zro_orientConstraint1" -p "input_constGrp";
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
	setAttr ".lr" -type "double3" 0 0 10 ;
	setAttr ".rsrr" -type "double3" 0 0 20 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "lowerLid_zro_orientConstraint1" -p "input_constGrp";
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
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
	setAttr -k on ".w0";
createNode pointConstraint -n "eyeLookAt_zro_pointConstraint1" -p "input_constGrp";
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
	setAttr ".o" -type "double3" 5 0 0 ;
	setAttr ".rst" -type "double3" 5.0000000000000009 0 -4.8985871965894118e-016 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "null4_orientConstraint1" -p "input_constGrp";
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
	setAttr ".lr" -type "double3" 0 0 -10 ;
	setAttr ".cpim" -type "matrix" 2.2204460492503126e-016 0 -1 0 0 1 0 0 1 0 2.2204460492503126e-016 0
		 0 0 0 1;
	setAttr ".rsrr" -type "double3" 0 0 -14.020000000000001 ;
	setAttr ".int" 2;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "output_grp" -p "rig_grp";
	rename -uid "CC58F5CF-4ED2-5712-6EAE-8692877BCC89";
	setAttr ".s" -type "double3" 0.99999999999999956 1 0.99999999999999956 ;
	setAttr ".it" no;
createNode joint -n "output_eye" -p "output_grp";
	rename -uid "4BFE705F-4CBD-30FB-BA9C-2E96924C06D6";
	setAttr ".t" -type "double3" 0 0 -5.9956194994587297e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -89.999999999999986 0 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eye";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode joint -n "output_eyeBall" -p "output_eye";
	rename -uid "5D7032B2-4D91-1C17-019A-6C85CB819C06";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "eyeBall";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode joint -n "output_iris" -p "output_eyeBall";
	rename -uid "976C1CB3-44B3-46E6-E711-E7B91EBB7737";
	setAttr ".t" -type "double3" 4.9999999999999991 0 -4.8985871965894138e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "iris";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode orientConstraint -n "output_eyeBall__orientConstraint1" -p "output_eyeBall";
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
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
	setAttr -k on ".w0";
createNode joint -n "output_upperLid" -p "output_eye";
	rename -uid "15429355-4069-2FA3-4413-F1B20EC27D53";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.3728319179984852e-016 2.4799562156788863e-015 19.999999999999996 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "upperLid";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode joint -n "output_upperLidEnd" -p "output_upperLid";
	rename -uid "F8640117-44E0-C07E-816B-F3919335EC52";
	setAttr ".t" -type "double3" 5.0000000000000009 6.6613381477509392e-016 -4.8985871965894118e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "upperLidEnd";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode orientConstraint -n "upperLid_orientConstraint1" -p "output_upperLid";
	rename -uid "8F4134A2-4CF6-FBA0-A7DA-20BE57A94805";
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
	setAttr ".lr" -type "double3" 0 0 -10.000000000000004 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
	setAttr -k on ".w1";
createNode joint -n "output_lowerLid" -p "output_eye";
	rename -uid "6D5291E9-4130-C789-73A8-65ABF35DFDB9";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.3728319179984852e-016 2.4799562156788863e-015 -19.999999999999996 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "lowerLid";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode joint -n "output_lowerLidEnd" -p "output_lowerLid";
	rename -uid "FC16CFF6-42D3-B8ED-BFBA-92AF6806357B";
	setAttr ".t" -type "double3" 5.0000000000000009 -6.6613381477509392e-016 -4.8985871965894118e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "lowerLidEnd";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode orientConstraint -n "lowerLid_orientConstraint1" -p "output_lowerLid";
	rename -uid "7B6CA9C7-473A-4422-61A2-818E07880711";
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
	setAttr ".lr" -type "double3" 0 0 9.5416640443905503e-015 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
	setAttr -k on ".w1";
createNode transform -n "const_grp" -p "rig_grp";
	rename -uid "275BBDDF-47EB-A231-6B46-4CAC6E681926";
createNode orientConstraint -n "upperLid_autoClose_orientConstraint1" -p "const_grp";
	rename -uid "C5F0C383-41BD-DF5B-3055-9096B2657793";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "upperLid_const_outW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr ".r" -type "double3" 0 0 10 ;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 0.99999999999999967 0.99999999999999978 1.0000000000000002 ;
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 3.1805546814635168e-015 ;
	setAttr ".rsrr" -type "double3" 0 0 5.862332965158866 ;
	setAttr ".int" 2;
	setAttr ".hio" yes;
	setAttr -k on ".w0";
createNode orientConstraint -n "lowerLid_autoClose_orientConstraint1" -p "const_grp";
	rename -uid "9CE53EA4-4383-8605-2AB7-1EBCF54720BC";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lowerLid_const_outW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr ".r" -type "double3" 0 0 -20 ;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 1 1.0000000000000004 1.0000000000000004 ;
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 0 -1.2722218725854067e-014 ;
	setAttr ".rsrr" -type "double3" 0 0 4.1214284852567769 ;
	setAttr ".int" 2;
	setAttr ".hio" yes;
	setAttr -k on ".w0";
createNode transform -s -n "persp";
	rename -uid "A5C283F2-46A9-9F52-AE19-B5B758A6A078";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -7.8700830634389405 3.7116591593627488 15.476487824972232 ;
	setAttr ".r" -type "double3" -14.738352729608774 -36.599999999999902 -9.9043517977307554e-016 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "6790D4F1-4466-128E-0555-1CB8A224A78C";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 13.982958268347216;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "F7FB7CBF-4638-D5B5-DF27-5DBACF65429C";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "FD7E20CC-43BF-5A44-B77C-DD97E158573F";
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
	rename -uid "148AAF42-4620-2B30-7B08-3B8178F4DA25";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "1743CDEF-41ED-84F3-CCEF-ACAF9A06D248";
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
	rename -uid "15319DEC-401A-A538-8BA7-B98568B4F62D";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "1A58F500-43EB-9FDB-39AD-6FBE975C04E1";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode cluster -n "cluster3";
	rename -uid "CD88247B-48D5-AC53-1CEC-37A43D615F43";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster3Set";
	rename -uid "3F9A1522-4E40-D781-3BA2-FBA8EE780089";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster3GroupId";
	rename -uid "41B7A4FC-4CF6-54AF-3BD4-C2803CEC39E9";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster3GroupParts";
	rename -uid "CDF383F9-4BDB-A454-B000-09AE51A9EF97";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode tweak -n "tweak3";
	rename -uid "46B55171-4004-50D8-587B-3FA8C11D343B";
createNode objectSet -n "tweakSet3";
	rename -uid "E254BA79-4BFE-35D7-4692-DE89BB9956A4";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId6";
	rename -uid "2B60A25F-4686-D4D6-3E7A-A4AC6008BD67";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts6";
	rename -uid "E7AC8937-440B-6639-64A4-739D10DA6C81";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "cluster1";
	rename -uid "AB9BF963-4A89-84B5-4D6D-C9BB33435A17";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 0.99999999999999989 0 0 0 0 0.99999999999999978 0 0
		 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster1Set";
	rename -uid "0FE3AB77-4ECD-E651-17EC-129CDC74AAFE";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster1GroupId";
	rename -uid "59B8DD75-4E6B-F2D5-4238-A6B546350FE9";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster1GroupParts";
	rename -uid "32C1952A-4D7C-1818-4638-31A222115098";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode tweak -n "tweak1";
	rename -uid "51B25F01-475F-9EA3-4D85-34B0AD40DD47";
createNode objectSet -n "tweakSet1";
	rename -uid "C28231B1-4E24-F089-C210-D081907DAD45";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	rename -uid "B6BE57B4-4318-1716-139E-25B2899A071C";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "CF8D4BD2-44A7-44FB-DBD3-9C9ECAF76651";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "cluster2";
	rename -uid "213B9B6D-4790-521C-241A-34B7B38AA5CF";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 0.99999999999999978 0 0 0 0 0.99999999999999978 0 0
		 0 0 0.99999999999999978 0 0 0 0 1;
createNode objectSet -n "cluster2Set";
	rename -uid "9540272C-4A00-E668-88F1-669043769193";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster2GroupId";
	rename -uid "D30104F9-485B-B6A8-29EB-8FA4D425A533";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster2GroupParts";
	rename -uid "DBCD94EF-4546-6403-067C-9198355D442E";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode tweak -n "tweak2";
	rename -uid "BC6C6AB2-4E7A-43D7-4EEE-A18C1423A5B7";
createNode objectSet -n "tweakSet2";
	rename -uid "8DB9DCE1-40CE-E5B2-8B78-16BC1DC58957";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId4";
	rename -uid "2B3B60AE-49C6-8A8A-04A0-4CA8C13A4CD7";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts4";
	rename -uid "E41BB55C-4AB3-3758-0861-D188F3CB1BCA";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "cluster4";
	rename -uid "765C86AE-415B-B54B-F8C6-97A9EB710EC5";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster4Set";
	rename -uid "7B3F4A7A-4685-8BEA-B15D-44B605BAF8D1";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster4GroupId";
	rename -uid "2EDAF7CC-4BD9-AC80-69DC-658A851B8781";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster4GroupParts";
	rename -uid "353429A4-4471-009D-470A-6ABAEBB5A6E4";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode tweak -n "tweak4";
	rename -uid "456749B2-42E7-0427-BFFB-B688D7D6F69F";
createNode objectSet -n "tweakSet4";
	rename -uid "4CA7BEBF-4519-68A3-0486-12819EFD0243";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId8";
	rename -uid "E3FAD3C8-494A-6B74-4908-2B85E72FE0A6";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts8";
	rename -uid "505C62BC-4068-E0F7-C625-75917DBD845E";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode animCurveUU -n "upperLid_autoFollow_result_orientConstraint1_eye_rotation_zroW1";
	rename -uid "8494A525-40F2-3C02-077F-DA94BBD6C852";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  0 1 1 0;
createNode animCurveUU -n "lowerLid_autoFollow_result_orientConstraint1_eye_rotation_zroW1";
	rename -uid "305ABFE3-4339-2565-B43B-92AA4F548226";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  0 1 1 0;
createNode unitConversion -n "unitConversion1";
	rename -uid "8E05DF16-48D5-B3E1-3EE8-F2BFBCC92601";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion2";
	rename -uid "9A378575-4758-B8F0-8B2A-63B34804CF9E";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion3";
	rename -uid "E0E5B8EB-415E-97C3-D923-1F968E19835C";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion4";
	rename -uid "41163E6D-42FD-E69A-B186-C5AAA721E638";
	setAttr ".cf" 0.017453292519943295;
createNode animCurveUU -n "upperLid_autoClose_result_orientConstraint1_upperLid_autoFollow_rotationW1";
	rename -uid "AACCD59D-4160-403D-879A-D1883EEF2A92";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  0 1 1 0;
createNode animCurveUU -n "lowerLid_autoClose_result_orientConstraint1_lowerLid_autoFollow_rotationW1";
	rename -uid "ADA3CFDD-4349-DF52-01A3-099CD4CDB583";
	setAttr ".tan" 2;
	setAttr -s 2 ".ktv[0:1]"  0 1 1 0;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "3493E89F-48B8-D9AD-FC63-FBA9AE550429";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "C95E7094-45F7-14D4-008E-EDA70795317E";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "4C87BB90-4159-7F7B-EAFA-ACB4B738AA47";
createNode displayLayerManager -n "layerManager";
	rename -uid "A4FAD56E-4F69-3FE6-95E4-268C6DCAB476";
createNode displayLayer -n "defaultLayer";
	rename -uid "67051467-4979-F9C3-1758-24BBBD44CA66";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "9E4BCE4A-4443-1ECD-B477-0FBA42C96825";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "5D251711-4619-C347-6941-B2BD6347A159";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "F640FBFA-4D8E-4671-80C8-1BA3FCF3CC3E";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n"
		+ "                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n"
		+ "                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1013\n                -height 877\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n"
		+ "            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n"
		+ "            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1013\n            -height 877\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n"
		+ "        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1013\\n    -height 877\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1013\\n    -height 877\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "FAFD5469-4B65-13B5-619E-B987EBC36D6A";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
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
connectAttr "eyeBall_grp_parentConstraint1.ctx" "module_grp.tx";
connectAttr "eyeBall_grp_parentConstraint1.cty" "module_grp.ty";
connectAttr "eyeBall_grp_parentConstraint1.ctz" "module_grp.tz";
connectAttr "eyeBall_grp_parentConstraint1.crx" "module_grp.rx";
connectAttr "eyeBall_grp_parentConstraint1.cry" "module_grp.ry";
connectAttr "eyeBall_grp_parentConstraint1.crz" "module_grp.rz";
connectAttr "eye_zro_orientConstraint1.crx" "eyeBall_zro.rx";
connectAttr "eye_zro_orientConstraint1.cry" "eyeBall_zro.ry";
connectAttr "eye_zro_orientConstraint1.crz" "eyeBall_zro.rz";
connectAttr "lookAt_result.r" "eyeBall_lookAt.r";
connectAttr "cluster3.og[0]" "eyeBall_FK_ctrlShape.cr";
connectAttr "tweak3.pl[0].cp[0]" "eyeBall_FK_ctrlShape.twl";
connectAttr "cluster3GroupId.id" "eyeBall_FK_ctrlShape.iog.og[3].gid";
connectAttr "cluster3Set.mwc" "eyeBall_FK_ctrlShape.iog.og[3].gco";
connectAttr "groupId6.id" "eyeBall_FK_ctrlShape.iog.og[4].gid";
connectAttr "tweakSet3.mwc" "eyeBall_FK_ctrlShape.iog.og[4].gco";
connectAttr "upperLid_zro_orientConstraint1.crx" "upperLid_zro.rx";
connectAttr "upperLid_zro_orientConstraint1.cry" "upperLid_zro.ry";
connectAttr "upperLid_zro_orientConstraint1.crz" "upperLid_zro.rz";
connectAttr "upperLid_autoFollow_result.r" "upperLid_autoFollow.r";
connectAttr "upperLid_autoClose_orientConstraint1.crx" "upperLid_autoClose.rx";
connectAttr "upperLid_autoClose_orientConstraint1.cry" "upperLid_autoClose.ry";
connectAttr "upperLid_autoClose_orientConstraint1.crz" "upperLid_autoClose.rz";
connectAttr "cluster1.og[0]" "upperLid_FK_ctrlShape.cr";
connectAttr "tweak1.pl[0].cp[0]" "upperLid_FK_ctrlShape.twl";
connectAttr "cluster1GroupId.id" "upperLid_FK_ctrlShape.iog.og[9].gid";
connectAttr "cluster1Set.mwc" "upperLid_FK_ctrlShape.iog.og[9].gco";
connectAttr "groupId2.id" "upperLid_FK_ctrlShape.iog.og[10].gid";
connectAttr "tweakSet1.mwc" "upperLid_FK_ctrlShape.iog.og[10].gco";
connectAttr "lowerLid_zro_orientConstraint1.crx" "lowerLid_zro.rx";
connectAttr "lowerLid_zro_orientConstraint1.cry" "lowerLid_zro.ry";
connectAttr "lowerLid_zro_orientConstraint1.crz" "lowerLid_zro.rz";
connectAttr "lowerLid_autoFollow_result.r" "lowerLid_autoFollow.r";
connectAttr "lowerLid_autoClose_orientConstraint1.crx" "lowerLid_autoClose.rx";
connectAttr "lowerLid_autoClose_orientConstraint1.cry" "lowerLid_autoClose.ry";
connectAttr "lowerLid_autoClose_orientConstraint1.crz" "lowerLid_autoClose.rz";
connectAttr "cluster2.og[0]" "lowerLid_FK_ctrlShape.cr";
connectAttr "tweak2.pl[0].cp[0]" "lowerLid_FK_ctrlShape.twl";
connectAttr "cluster2GroupId.id" "lowerLid_FK_ctrlShape.iog.og[8].gid";
connectAttr "cluster2Set.mwc" "lowerLid_FK_ctrlShape.iog.og[8].gco";
connectAttr "groupId4.id" "lowerLid_FK_ctrlShape.iog.og[9].gid";
connectAttr "tweakSet2.mwc" "lowerLid_FK_ctrlShape.iog.og[9].gco";
connectAttr "eyeLookAt_zro_pointConstraint1.ctz" "lookAt_zro.tz";
connectAttr "eyeLookAt_zro_pointConstraint1.ctx" "lookAt_zro.tx";
connectAttr "eyeLookAt_zro_pointConstraint1.cty" "lookAt_zro.ty";
connectAttr "cluster4.og[0]" "autoClose_ctrlShape.cr";
connectAttr "tweak4.pl[0].cp[0]" "autoClose_ctrlShape.twl";
connectAttr "cluster4GroupId.id" "autoClose_ctrlShape.iog.og[0].gid";
connectAttr "cluster4Set.mwc" "autoClose_ctrlShape.iog.og[0].gco";
connectAttr "groupId8.id" "autoClose_ctrlShape.iog.og[1].gid";
connectAttr "tweakSet4.mwc" "autoClose_ctrlShape.iog.og[1].gco";
connectAttr "eye_lookAtRig_grp_orientConstraint1.crx" "lookAtRig_grp.rx";
connectAttr "eye_lookAtRig_grp_orientConstraint1.cry" "lookAtRig_grp.ry";
connectAttr "eye_lookAtRig_grp_orientConstraint1.crz" "lookAtRig_grp.rz";
connectAttr "eye_lookAt_result_aimConstraint1.crx" "lookAt_result.rx";
connectAttr "eye_lookAt_result_aimConstraint1.cry" "lookAt_result.ry";
connectAttr "eye_lookAt_result_aimConstraint1.crz" "lookAt_result.rz";
connectAttr "lookAt_result.pim" "eye_lookAt_result_aimConstraint1.cpim";
connectAttr "lookAt_result.t" "eye_lookAt_result_aimConstraint1.ct";
connectAttr "lookAt_result.rp" "eye_lookAt_result_aimConstraint1.crp";
connectAttr "lookAt_result.rpt" "eye_lookAt_result_aimConstraint1.crt";
connectAttr "lookAt_result.ro" "eye_lookAt_result_aimConstraint1.cro";
connectAttr "lookAt_ctrl.t" "eye_lookAt_result_aimConstraint1.tg[0].tt";
connectAttr "lookAt_ctrl.rp" "eye_lookAt_result_aimConstraint1.tg[0].trp";
connectAttr "lookAt_ctrl.rpt" "eye_lookAt_result_aimConstraint1.tg[0].trt";
connectAttr "lookAt_ctrl.pm" "eye_lookAt_result_aimConstraint1.tg[0].tpm";
connectAttr "eye_lookAt_result_aimConstraint1.w0" "eye_lookAt_result_aimConstraint1.tg[0].tw"
		;
connectAttr "lookAtRig_grp.wm" "eye_lookAt_result_aimConstraint1.wum";
connectAttr "eyeBall_zro.r" "eye_rotation_zro.r";
connectAttr "eye_rotation_orientConstraint1.crx" "eye_rotation.rx";
connectAttr "eye_rotation_orientConstraint1.cry" "eye_rotation.ry";
connectAttr "eye_rotation_orientConstraint1.crz" "eye_rotation.rz";
connectAttr "eye_rotation.ro" "eye_rotation_orientConstraint1.cro";
connectAttr "eye_rotation.pim" "eye_rotation_orientConstraint1.cpim";
connectAttr "eyeBall_constrainJnt.r" "eye_rotation_orientConstraint1.tg[0].tr";
connectAttr "eyeBall_constrainJnt.ro" "eye_rotation_orientConstraint1.tg[0].tro"
		;
connectAttr "eyeBall_constrainJnt.pm" "eye_rotation_orientConstraint1.tg[0].tpm"
		;
connectAttr "eye_rotation_orientConstraint1.w0" "eye_rotation_orientConstraint1.tg[0].tw"
		;
connectAttr "upperLid_autoFollow_result_orientConstraint1.crz" "upperLid_autoFollow_result.rz"
		;
connectAttr "upperLid_autoFollow_result_orientConstraint1.crx" "upperLid_autoFollow_result.rx"
		;
connectAttr "upperLid_autoFollow_result_orientConstraint1.cry" "upperLid_autoFollow_result.ry"
		;
connectAttr "upperLid_maxRotation.rz" "upperLid_autoFollow_result.xrzl";
connectAttr "upperLid_minRotation.rz" "upperLid_autoFollow_result.mrzl";
connectAttr "upperLid_autoFollow_result.ro" "upperLid_autoFollow_result_orientConstraint1.cro"
		;
connectAttr "upperLid_autoFollow_result.pim" "upperLid_autoFollow_result_orientConstraint1.cpim"
		;
connectAttr "eye_rotation.r" "upperLid_autoFollow_result_orientConstraint1.tg[0].tr"
		;
connectAttr "eye_rotation.ro" "upperLid_autoFollow_result_orientConstraint1.tg[0].tro"
		;
connectAttr "eye_rotation.pm" "upperLid_autoFollow_result_orientConstraint1.tg[0].tpm"
		;
connectAttr "upperLid_autoFollow_result_orientConstraint1.w0" "upperLid_autoFollow_result_orientConstraint1.tg[0].tw"
		;
connectAttr "eye_rotation_zro.r" "upperLid_autoFollow_result_orientConstraint1.tg[1].tr"
		;
connectAttr "eye_rotation_zro.ro" "upperLid_autoFollow_result_orientConstraint1.tg[1].tro"
		;
connectAttr "eye_rotation_zro.pm" "upperLid_autoFollow_result_orientConstraint1.tg[1].tpm"
		;
connectAttr "upperLid_autoFollow_result_orientConstraint1.w1" "upperLid_autoFollow_result_orientConstraint1.tg[1].tw"
		;
connectAttr "upperLid_FK_ctrl.autoFollow_weight" "upperLid_autoFollow_result_orientConstraint1.w0"
		;
connectAttr "upperLid_autoFollow_result_orientConstraint1_eye_rotation_zroW1.o" "upperLid_autoFollow_result_orientConstraint1.w1"
		;
connectAttr "lowerLid_autoFollow_result_orientConstraint1.crz" "lowerLid_autoFollow_result.rz"
		;
connectAttr "lowerLid_autoFollow_result_orientConstraint1.crx" "lowerLid_autoFollow_result.rx"
		;
connectAttr "lowerLid_autoFollow_result_orientConstraint1.cry" "lowerLid_autoFollow_result.ry"
		;
connectAttr "lowerLid_maxRotation.rz" "lowerLid_autoFollow_result.xrzl";
connectAttr "lowerLid_minRotation.rz" "lowerLid_autoFollow_result.mrzl";
connectAttr "lowerLid_autoFollow_result.ro" "lowerLid_autoFollow_result_orientConstraint1.cro"
		;
connectAttr "lowerLid_autoFollow_result.pim" "lowerLid_autoFollow_result_orientConstraint1.cpim"
		;
connectAttr "eye_rotation.r" "lowerLid_autoFollow_result_orientConstraint1.tg[0].tr"
		;
connectAttr "eye_rotation.ro" "lowerLid_autoFollow_result_orientConstraint1.tg[0].tro"
		;
connectAttr "eye_rotation.pm" "lowerLid_autoFollow_result_orientConstraint1.tg[0].tpm"
		;
connectAttr "lowerLid_autoFollow_result_orientConstraint1.w0" "lowerLid_autoFollow_result_orientConstraint1.tg[0].tw"
		;
connectAttr "eye_rotation_zro.r" "lowerLid_autoFollow_result_orientConstraint1.tg[1].tr"
		;
connectAttr "eye_rotation_zro.ro" "lowerLid_autoFollow_result_orientConstraint1.tg[1].tro"
		;
connectAttr "eye_rotation_zro.pm" "lowerLid_autoFollow_result_orientConstraint1.tg[1].tpm"
		;
connectAttr "lowerLid_autoFollow_result_orientConstraint1.w1" "lowerLid_autoFollow_result_orientConstraint1.tg[1].tw"
		;
connectAttr "lowerLid_FK_ctrl.autoFollow_weight" "lowerLid_autoFollow_result_orientConstraint1.w0"
		;
connectAttr "lowerLid_autoFollow_result_orientConstraint1_eye_rotation_zroW1.o" "lowerLid_autoFollow_result_orientConstraint1.w1"
		;
connectAttr "upperLid_zro.r" "upperLid_rotation_zro.r";
connectAttr "unitConversion1.o" "upperLid_maxRotation.rz";
connectAttr "unitConversion2.o" "upperLid_minRotation.rz";
connectAttr "upperLid_autoFollow_result.r" "upperLid_rotation.r";
connectAttr "lowerLid_zro.r" "lowerLid_rotation_zro.r";
connectAttr "unitConversion3.o" "lowerLid_maxRotation.rz";
connectAttr "unitConversion4.o" "lowerLid_minRotation.rz";
connectAttr "lowerLid_autoFollow_result.r" "lowerLid_rotation.r";
connectAttr "autoClose_ctrl.close" "autoLidCloseRig_grp.close";
connectAttr "upperLid_autoFollow_rotation_orientConstraint1.crx" "upperLid_autoFollow_rotation.rx"
		;
connectAttr "upperLid_autoFollow_rotation_orientConstraint1.cry" "upperLid_autoFollow_rotation.ry"
		;
connectAttr "upperLid_autoFollow_rotation_orientConstraint1.crz" "upperLid_autoFollow_rotation.rz"
		;
connectAttr "upperLid_autoFollow_rotation.ro" "upperLid_autoFollow_rotation_orientConstraint1.cro"
		;
connectAttr "upperLid_autoFollow_rotation.pim" "upperLid_autoFollow_rotation_orientConstraint1.cpim"
		;
connectAttr "upperLid_autoFollow.r" "upperLid_autoFollow_rotation_orientConstraint1.tg[0].tr"
		;
connectAttr "upperLid_autoFollow.ro" "upperLid_autoFollow_rotation_orientConstraint1.tg[0].tro"
		;
connectAttr "upperLid_autoFollow.pm" "upperLid_autoFollow_rotation_orientConstraint1.tg[0].tpm"
		;
connectAttr "upperLid_autoFollow_rotation_orientConstraint1.w0" "upperLid_autoFollow_rotation_orientConstraint1.tg[0].tw"
		;
connectAttr "lowerLid_autoFollow_rotation_orientConstraint1.crx" "lowerLid_autoFollow_rotation.rx"
		;
connectAttr "lowerLid_autoFollow_rotation_orientConstraint1.cry" "lowerLid_autoFollow_rotation.ry"
		;
connectAttr "lowerLid_autoFollow_rotation_orientConstraint1.crz" "lowerLid_autoFollow_rotation.rz"
		;
connectAttr "lowerLid_autoFollow_rotation.ro" "lowerLid_autoFollow_rotation_orientConstraint1.cro"
		;
connectAttr "lowerLid_autoFollow_rotation.pim" "lowerLid_autoFollow_rotation_orientConstraint1.cpim"
		;
connectAttr "lowerLid_autoFollow.r" "lowerLid_autoFollow_rotation_orientConstraint1.tg[0].tr"
		;
connectAttr "lowerLid_autoFollow.ro" "lowerLid_autoFollow_rotation_orientConstraint1.tg[0].tro"
		;
connectAttr "lowerLid_autoFollow.pm" "lowerLid_autoFollow_rotation_orientConstraint1.tg[0].tpm"
		;
connectAttr "lowerLid_autoFollow_rotation_orientConstraint1.w0" "lowerLid_autoFollow_rotation_orientConstraint1.tg[0].tw"
		;
connectAttr "upperLid_autoClose_result_orientConstraint1.crx" "upperLid_autoClose_result.rx"
		;
connectAttr "upperLid_autoClose_result_orientConstraint1.cry" "upperLid_autoClose_result.ry"
		;
connectAttr "upperLid_autoClose_result_orientConstraint1.crz" "upperLid_autoClose_result.rz"
		;
connectAttr "upperLid_autoClose_result.ro" "upperLid_autoClose_result_orientConstraint1.cro"
		;
connectAttr "upperLid_autoClose_result.pim" "upperLid_autoClose_result_orientConstraint1.cpim"
		;
connectAttr "lid_autoClose_rotation.r" "upperLid_autoClose_result_orientConstraint1.tg[0].tr"
		;
connectAttr "lid_autoClose_rotation.ro" "upperLid_autoClose_result_orientConstraint1.tg[0].tro"
		;
connectAttr "lid_autoClose_rotation.pm" "upperLid_autoClose_result_orientConstraint1.tg[0].tpm"
		;
connectAttr "upperLid_autoClose_result_orientConstraint1.w0" "upperLid_autoClose_result_orientConstraint1.tg[0].tw"
		;
connectAttr "upperLid_autoFollow_rotation.r" "upperLid_autoClose_result_orientConstraint1.tg[1].tr"
		;
connectAttr "upperLid_autoFollow_rotation.ro" "upperLid_autoClose_result_orientConstraint1.tg[1].tro"
		;
connectAttr "upperLid_autoFollow_rotation.pm" "upperLid_autoClose_result_orientConstraint1.tg[1].tpm"
		;
connectAttr "upperLid_autoClose_result_orientConstraint1.w1" "upperLid_autoClose_result_orientConstraint1.tg[1].tw"
		;
connectAttr "autoLidCloseRig_grp.close" "upperLid_autoClose_result_orientConstraint1.w0"
		;
connectAttr "upperLid_autoClose_result_orientConstraint1_upperLid_autoFollow_rotationW1.o" "upperLid_autoClose_result_orientConstraint1.w1"
		;
connectAttr "lowerLid_autoClose_result_orientConstraint1.crx" "lowerLid_autoClose_result.rx"
		;
connectAttr "lowerLid_autoClose_result_orientConstraint1.cry" "lowerLid_autoClose_result.ry"
		;
connectAttr "lowerLid_autoClose_result_orientConstraint1.crz" "lowerLid_autoClose_result.rz"
		;
connectAttr "lowerLid_autoClose_result.ro" "lowerLid_autoClose_result_orientConstraint1.cro"
		;
connectAttr "lowerLid_autoClose_result.pim" "lowerLid_autoClose_result_orientConstraint1.cpim"
		;
connectAttr "lid_autoClose_rotation.r" "lowerLid_autoClose_result_orientConstraint1.tg[0].tr"
		;
connectAttr "lid_autoClose_rotation.ro" "lowerLid_autoClose_result_orientConstraint1.tg[0].tro"
		;
connectAttr "lid_autoClose_rotation.pm" "lowerLid_autoClose_result_orientConstraint1.tg[0].tpm"
		;
connectAttr "lowerLid_autoClose_result_orientConstraint1.w0" "lowerLid_autoClose_result_orientConstraint1.tg[0].tw"
		;
connectAttr "lowerLid_autoFollow_rotation.r" "lowerLid_autoClose_result_orientConstraint1.tg[1].tr"
		;
connectAttr "lowerLid_autoFollow_rotation.ro" "lowerLid_autoClose_result_orientConstraint1.tg[1].tro"
		;
connectAttr "lowerLid_autoFollow_rotation.pm" "lowerLid_autoClose_result_orientConstraint1.tg[1].tpm"
		;
connectAttr "lowerLid_autoClose_result_orientConstraint1.w1" "lowerLid_autoClose_result_orientConstraint1.tg[1].tw"
		;
connectAttr "autoLidCloseRig_grp.close" "lowerLid_autoClose_result_orientConstraint1.w0"
		;
connectAttr "lowerLid_autoClose_result_orientConstraint1_lowerLid_autoFollow_rotationW1.o" "lowerLid_autoClose_result_orientConstraint1.w1"
		;
connectAttr "eyeBall_zro.r" "clst_eyeZro_grp.r";
connectAttr "input_iris.t" "cluster3Handle.t";
connectAttr "upperLid_zro.r" "clst_upperLidZro_grp.r";
connectAttr "input_upperLidEnd.t" "cluster1Handle.t";
connectAttr "lowerLid_zro.r" "clst_lowerLidZro_grp.r";
connectAttr "input_lowerLidEnd.t" "cluster2Handle.t";
connectAttr "input_iris.tx" "cluster4Handle.sx";
connectAttr "input_iris.tx" "cluster4Handle.sy";
connectAttr "input_iris.tx" "cluster4Handle.sz";
connectAttr "input_eye.s" "input_eyeBall.is";
connectAttr "input_eyeBall.s" "input_iris.is";
connectAttr "input_eye.s" "input_upperLid.is";
connectAttr "input_upperLid.s" "input_upperLidEnd.is";
connectAttr "input_eye.s" "input_lowerLid.is";
connectAttr "input_lowerLid.s" "input_lowerLidEnd.is";
connectAttr "module_grp.ro" "eyeBall_grp_parentConstraint1.cro";
connectAttr "module_grp.pim" "eyeBall_grp_parentConstraint1.cpim";
connectAttr "module_grp.rp" "eyeBall_grp_parentConstraint1.crp";
connectAttr "module_grp.rpt" "eyeBall_grp_parentConstraint1.crt";
connectAttr "input_eye.t" "eyeBall_grp_parentConstraint1.tg[0].tt";
connectAttr "input_eye.rp" "eyeBall_grp_parentConstraint1.tg[0].trp";
connectAttr "input_eye.rpt" "eyeBall_grp_parentConstraint1.tg[0].trt";
connectAttr "input_eye.r" "eyeBall_grp_parentConstraint1.tg[0].tr";
connectAttr "input_eye.ro" "eyeBall_grp_parentConstraint1.tg[0].tro";
connectAttr "input_eye.s" "eyeBall_grp_parentConstraint1.tg[0].ts";
connectAttr "input_eye.pm" "eyeBall_grp_parentConstraint1.tg[0].tpm";
connectAttr "input_eye.jo" "eyeBall_grp_parentConstraint1.tg[0].tjo";
connectAttr "input_eye.ssc" "eyeBall_grp_parentConstraint1.tg[0].tsc";
connectAttr "input_eye.is" "eyeBall_grp_parentConstraint1.tg[0].tis";
connectAttr "eyeBall_grp_parentConstraint1.w0" "eyeBall_grp_parentConstraint1.tg[0].tw"
		;
connectAttr "lookAtRig_grp.ro" "eye_lookAtRig_grp_orientConstraint1.cro";
connectAttr "lookAtRig_grp.pim" "eye_lookAtRig_grp_orientConstraint1.cpim";
connectAttr "input_eyeBall.r" "eye_lookAtRig_grp_orientConstraint1.tg[0].tr";
connectAttr "input_eyeBall.ro" "eye_lookAtRig_grp_orientConstraint1.tg[0].tro";
connectAttr "input_eyeBall.pm" "eye_lookAtRig_grp_orientConstraint1.tg[0].tpm";
connectAttr "input_eyeBall.jo" "eye_lookAtRig_grp_orientConstraint1.tg[0].tjo";
connectAttr "eye_lookAtRig_grp_orientConstraint1.w0" "eye_lookAtRig_grp_orientConstraint1.tg[0].tw"
		;
connectAttr "eyeBall_zro.ro" "eye_zro_orientConstraint1.cro";
connectAttr "eyeBall_zro.pim" "eye_zro_orientConstraint1.cpim";
connectAttr "input_eyeBall.r" "eye_zro_orientConstraint1.tg[0].tr";
connectAttr "input_eyeBall.ro" "eye_zro_orientConstraint1.tg[0].tro";
connectAttr "input_eyeBall.pm" "eye_zro_orientConstraint1.tg[0].tpm";
connectAttr "input_eyeBall.jo" "eye_zro_orientConstraint1.tg[0].tjo";
connectAttr "eye_zro_orientConstraint1.w0" "eye_zro_orientConstraint1.tg[0].tw";
connectAttr "upperLid_zro.ro" "upperLid_zro_orientConstraint1.cro";
connectAttr "upperLid_zro.pim" "upperLid_zro_orientConstraint1.cpim";
connectAttr "input_upperLid.r" "upperLid_zro_orientConstraint1.tg[0].tr";
connectAttr "input_upperLid.ro" "upperLid_zro_orientConstraint1.tg[0].tro";
connectAttr "input_upperLid.pm" "upperLid_zro_orientConstraint1.tg[0].tpm";
connectAttr "input_upperLid.jo" "upperLid_zro_orientConstraint1.tg[0].tjo";
connectAttr "upperLid_zro_orientConstraint1.w0" "upperLid_zro_orientConstraint1.tg[0].tw"
		;
connectAttr "lowerLid_zro.ro" "lowerLid_zro_orientConstraint1.cro";
connectAttr "lowerLid_zro.pim" "lowerLid_zro_orientConstraint1.cpim";
connectAttr "input_lowerLid.r" "lowerLid_zro_orientConstraint1.tg[0].tr";
connectAttr "input_lowerLid.ro" "lowerLid_zro_orientConstraint1.tg[0].tro";
connectAttr "input_lowerLid.pm" "lowerLid_zro_orientConstraint1.tg[0].tpm";
connectAttr "input_lowerLid.jo" "lowerLid_zro_orientConstraint1.tg[0].tjo";
connectAttr "lowerLid_zro_orientConstraint1.w0" "lowerLid_zro_orientConstraint1.tg[0].tw"
		;
connectAttr "lookAt_zro.pim" "eyeLookAt_zro_pointConstraint1.cpim";
connectAttr "lookAt_zro.rp" "eyeLookAt_zro_pointConstraint1.crp";
connectAttr "lookAt_zro.rpt" "eyeLookAt_zro_pointConstraint1.crt";
connectAttr "input_iris.t" "eyeLookAt_zro_pointConstraint1.tg[0].tt";
connectAttr "input_iris.rp" "eyeLookAt_zro_pointConstraint1.tg[0].trp";
connectAttr "input_iris.rpt" "eyeLookAt_zro_pointConstraint1.tg[0].trt";
connectAttr "input_iris.pm" "eyeLookAt_zro_pointConstraint1.tg[0].tpm";
connectAttr "eyeLookAt_zro_pointConstraint1.w0" "eyeLookAt_zro_pointConstraint1.tg[0].tw"
		;
connectAttr "input_eyeBall.r" "null4_orientConstraint1.tg[0].tr";
connectAttr "input_eyeBall.ro" "null4_orientConstraint1.tg[0].tro";
connectAttr "input_eyeBall.pm" "null4_orientConstraint1.tg[0].tpm";
connectAttr "input_eyeBall.jo" "null4_orientConstraint1.tg[0].tjo";
connectAttr "null4_orientConstraint1.w0" "null4_orientConstraint1.tg[0].tw";
connectAttr "input_lowerLid.r" "null4_orientConstraint1.tg[1].tr";
connectAttr "input_lowerLid.ro" "null4_orientConstraint1.tg[1].tro";
connectAttr "input_lowerLid.pm" "null4_orientConstraint1.tg[1].tpm";
connectAttr "input_lowerLid.jo" "null4_orientConstraint1.tg[1].tjo";
connectAttr "null4_orientConstraint1.w1" "null4_orientConstraint1.tg[1].tw";
connectAttr "output_eye.s" "output_eyeBall.is";
connectAttr "output_eyeBall__orientConstraint1.crx" "output_eyeBall.rx";
connectAttr "output_eyeBall__orientConstraint1.cry" "output_eyeBall.ry";
connectAttr "output_eyeBall__orientConstraint1.crz" "output_eyeBall.rz";
connectAttr "output_eyeBall.s" "output_iris.is";
connectAttr "output_eyeBall.ro" "output_eyeBall__orientConstraint1.cro";
connectAttr "output_eyeBall.pim" "output_eyeBall__orientConstraint1.cpim";
connectAttr "output_eyeBall.jo" "output_eyeBall__orientConstraint1.cjo";
connectAttr "output_eyeBall.is" "output_eyeBall__orientConstraint1.is";
connectAttr "eyeBall_constrainJnt.r" "output_eyeBall__orientConstraint1.tg[0].tr"
		;
connectAttr "eyeBall_constrainJnt.ro" "output_eyeBall__orientConstraint1.tg[0].tro"
		;
connectAttr "eyeBall_constrainJnt.pm" "output_eyeBall__orientConstraint1.tg[0].tpm"
		;
connectAttr "output_eyeBall__orientConstraint1.w0" "output_eyeBall__orientConstraint1.tg[0].tw"
		;
connectAttr "output_eye.s" "output_upperLid.is";
connectAttr "upperLid_orientConstraint1.crx" "output_upperLid.rx";
connectAttr "upperLid_orientConstraint1.cry" "output_upperLid.ry";
connectAttr "upperLid_orientConstraint1.crz" "output_upperLid.rz";
connectAttr "output_upperLid.s" "output_upperLidEnd.is";
connectAttr "output_upperLid.ro" "upperLid_orientConstraint1.cro";
connectAttr "output_upperLid.pim" "upperLid_orientConstraint1.cpim";
connectAttr "output_upperLid.jo" "upperLid_orientConstraint1.cjo";
connectAttr "output_upperLid.is" "upperLid_orientConstraint1.is";
connectAttr "upperLid_constrainJnt.r" "upperLid_orientConstraint1.tg[1].tr";
connectAttr "upperLid_constrainJnt.ro" "upperLid_orientConstraint1.tg[1].tro";
connectAttr "upperLid_constrainJnt.pm" "upperLid_orientConstraint1.tg[1].tpm";
connectAttr "upperLid_orientConstraint1.w1" "upperLid_orientConstraint1.tg[1].tw"
		;
connectAttr "output_eye.s" "output_lowerLid.is";
connectAttr "lowerLid_orientConstraint1.crx" "output_lowerLid.rx";
connectAttr "lowerLid_orientConstraint1.cry" "output_lowerLid.ry";
connectAttr "lowerLid_orientConstraint1.crz" "output_lowerLid.rz";
connectAttr "output_lowerLid.s" "output_lowerLidEnd.is";
connectAttr "output_lowerLid.ro" "lowerLid_orientConstraint1.cro";
connectAttr "output_lowerLid.pim" "lowerLid_orientConstraint1.cpim";
connectAttr "output_lowerLid.jo" "lowerLid_orientConstraint1.cjo";
connectAttr "output_lowerLid.is" "lowerLid_orientConstraint1.is";
connectAttr "lowerLid_constrainJnt.r" "lowerLid_orientConstraint1.tg[1].tr";
connectAttr "lowerLid_constrainJnt.ro" "lowerLid_orientConstraint1.tg[1].tro";
connectAttr "lowerLid_constrainJnt.pm" "lowerLid_orientConstraint1.tg[1].tpm";
connectAttr "lowerLid_orientConstraint1.w1" "lowerLid_orientConstraint1.tg[1].tw"
		;
connectAttr "upperLid_autoClose.ro" "upperLid_autoClose_orientConstraint1.cro";
connectAttr "upperLid_autoClose.pim" "upperLid_autoClose_orientConstraint1.cpim"
		;
connectAttr "upperLid_autoClose_result.r" "upperLid_autoClose_orientConstraint1.tg[0].tr"
		;
connectAttr "upperLid_autoClose_result.ro" "upperLid_autoClose_orientConstraint1.tg[0].tro"
		;
connectAttr "upperLid_autoClose_result.pm" "upperLid_autoClose_orientConstraint1.tg[0].tpm"
		;
connectAttr "upperLid_autoClose_orientConstraint1.w0" "upperLid_autoClose_orientConstraint1.tg[0].tw"
		;
connectAttr "lowerLid_autoClose.ro" "lowerLid_autoClose_orientConstraint1.cro";
connectAttr "lowerLid_autoClose.pim" "lowerLid_autoClose_orientConstraint1.cpim"
		;
connectAttr "lowerLid_autoClose_result.r" "lowerLid_autoClose_orientConstraint1.tg[0].tr"
		;
connectAttr "lowerLid_autoClose_result.ro" "lowerLid_autoClose_orientConstraint1.tg[0].tro"
		;
connectAttr "lowerLid_autoClose_result.pm" "lowerLid_autoClose_orientConstraint1.tg[0].tpm"
		;
connectAttr "lowerLid_autoClose_orientConstraint1.w0" "lowerLid_autoClose_orientConstraint1.tg[0].tw"
		;
connectAttr "cluster3GroupParts.og" "cluster3.ip[0].ig";
connectAttr "cluster3GroupId.id" "cluster3.ip[0].gi";
connectAttr "cluster3Handle.wm" "cluster3.ma";
connectAttr "cluster3HandleShape.x" "cluster3.x";
connectAttr "cluster3GroupId.msg" "cluster3Set.gn" -na;
connectAttr "eyeBall_FK_ctrlShape.iog.og[3]" "cluster3Set.dsm" -na;
connectAttr "cluster3.msg" "cluster3Set.ub[0]";
connectAttr "tweak3.og[0]" "cluster3GroupParts.ig";
connectAttr "cluster3GroupId.id" "cluster3GroupParts.gi";
connectAttr "groupParts6.og" "tweak3.ip[0].ig";
connectAttr "groupId6.id" "tweak3.ip[0].gi";
connectAttr "groupId6.msg" "tweakSet3.gn" -na;
connectAttr "eyeBall_FK_ctrlShape.iog.og[4]" "tweakSet3.dsm" -na;
connectAttr "tweak3.msg" "tweakSet3.ub[0]";
connectAttr "eyeBall_FK_ctrlShapeOrig.ws" "groupParts6.ig";
connectAttr "groupId6.id" "groupParts6.gi";
connectAttr "cluster1GroupParts.og" "cluster1.ip[0].ig";
connectAttr "cluster1GroupId.id" "cluster1.ip[0].gi";
connectAttr "cluster1Handle.wm" "cluster1.ma";
connectAttr "cluster1HandleShape.x" "cluster1.x";
connectAttr "cluster1GroupId.msg" "cluster1Set.gn" -na;
connectAttr "upperLid_FK_ctrlShape.iog.og[9]" "cluster1Set.dsm" -na;
connectAttr "cluster1.msg" "cluster1Set.ub[0]";
connectAttr "tweak1.og[0]" "cluster1GroupParts.ig";
connectAttr "cluster1GroupId.id" "cluster1GroupParts.gi";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "upperLid_FK_ctrlShape.iog.og[10]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "upperLid_FK_ctrlShapeOrig.ws" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "cluster2GroupParts.og" "cluster2.ip[0].ig";
connectAttr "cluster2GroupId.id" "cluster2.ip[0].gi";
connectAttr "cluster2Handle.wm" "cluster2.ma";
connectAttr "cluster2HandleShape.x" "cluster2.x";
connectAttr "cluster2GroupId.msg" "cluster2Set.gn" -na;
connectAttr "lowerLid_FK_ctrlShape.iog.og[8]" "cluster2Set.dsm" -na;
connectAttr "cluster2.msg" "cluster2Set.ub[0]";
connectAttr "tweak2.og[0]" "cluster2GroupParts.ig";
connectAttr "cluster2GroupId.id" "cluster2GroupParts.gi";
connectAttr "groupParts4.og" "tweak2.ip[0].ig";
connectAttr "groupId4.id" "tweak2.ip[0].gi";
connectAttr "groupId4.msg" "tweakSet2.gn" -na;
connectAttr "lowerLid_FK_ctrlShape.iog.og[9]" "tweakSet2.dsm" -na;
connectAttr "tweak2.msg" "tweakSet2.ub[0]";
connectAttr "lowerLid_FK_ctrlShapeOrig.ws" "groupParts4.ig";
connectAttr "groupId4.id" "groupParts4.gi";
connectAttr "cluster4GroupParts.og" "cluster4.ip[0].ig";
connectAttr "cluster4GroupId.id" "cluster4.ip[0].gi";
connectAttr "cluster4Handle.wm" "cluster4.ma";
connectAttr "cluster4HandleShape.x" "cluster4.x";
connectAttr "cluster4GroupId.msg" "cluster4Set.gn" -na;
connectAttr "autoClose_ctrlShape.iog.og[0]" "cluster4Set.dsm" -na;
connectAttr "cluster4.msg" "cluster4Set.ub[0]";
connectAttr "tweak4.og[0]" "cluster4GroupParts.ig";
connectAttr "cluster4GroupId.id" "cluster4GroupParts.gi";
connectAttr "groupParts8.og" "tweak4.ip[0].ig";
connectAttr "groupId8.id" "tweak4.ip[0].gi";
connectAttr "groupId8.msg" "tweakSet4.gn" -na;
connectAttr "autoClose_ctrlShape.iog.og[1]" "tweakSet4.dsm" -na;
connectAttr "tweak4.msg" "tweakSet4.ub[0]";
connectAttr "autoClose_ctrlShapeOrig.ws" "groupParts8.ig";
connectAttr "groupId8.id" "groupParts8.gi";
connectAttr "upperLid_autoFollow_result_orientConstraint1.w0" "upperLid_autoFollow_result_orientConstraint1_eye_rotation_zroW1.i"
		;
connectAttr "lowerLid_autoFollow_result_orientConstraint1.w0" "lowerLid_autoFollow_result_orientConstraint1_eye_rotation_zroW1.i"
		;
connectAttr "upperLid_FK_ctrl.autoFollow_max" "unitConversion1.i";
connectAttr "upperLid_FK_ctrl.autoFollow_min" "unitConversion2.i";
connectAttr "lowerLid_FK_ctrl.autoFollow_max" "unitConversion3.i";
connectAttr "lowerLid_FK_ctrl.autoFollow_min" "unitConversion4.i";
connectAttr "upperLid_autoClose_result_orientConstraint1.w0" "upperLid_autoClose_result_orientConstraint1_upperLid_autoFollow_rotationW1.i"
		;
connectAttr "lowerLid_autoClose_result_orientConstraint1.w0" "lowerLid_autoClose_result_orientConstraint1_lowerLid_autoFollow_rotationW1.i"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of eye_rig.ma
