//Maya ASCII 2017 scene
//Name: head_template.ma
//Last modified: Fri, Nov 04, 2016 06:12:30 PM
//Codeset: 949
requires maya "2017";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201608291545-1001872";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -n "root";
	rename -uid "C91747A4-4198-978C-2AC3-FD98C03BE128";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" -5.9787338831956039e-016 5 2 ;
	setAttr ".r" -type "double3" -89.999999999999972 0 89.999999999999972 ;
	setAttr ".dh" yes;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "hdl_grp" -p "root";
	rename -uid "9C3F89A6-4C27-50BB-38DF-908ABEBAD7EA";
createNode transform -n "head_up_zro" -p "hdl_grp";
	rename -uid "220B765D-446A-9586-D049-8BAB94226F1C";
	setAttr ".t" -type "double3" 12 -2.2204460492503131e-015 3.8031680382394827e-015 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "head_up" -p "head_up_zro";
	rename -uid "8E02FCB7-40A3-2770-73CD-539E63092068";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".dh" yes;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.5 0.5 0 ;
createNode nurbsCurve -n "head_upShape" -p "head_up";
	rename -uid "8CEDBFBD-431F-9E03-DBD9-859AF4437864";
	addAttr -s false -ci true -sn "curveConnectedTo" -ln "curveConnectedTo" -at "message";
	addAttr -s false -ci true -sn "curveConnectedLOC" -ln "curveConnectedLOC" -at "message";
	addAttr -s false -ci true -sn "curveConnectedOrgShape" -ln "curveConnectedOrgShape" 
		-at "message";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		-1.9998000199980002 4.4408920985006262e-016 -3.7900397590393027e-015
		;
	setAttr ".ipo" yes;
createNode nurbsCurve -n "head_upShapeOriginal" -p "head_up";
	rename -uid "94F35EA1-4CFB-3429-0C91-EDA37C2186F2";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		0 0 0
		;
createNode transform -n "head_back_zro" -p "hdl_grp";
	rename -uid "307931A0-41B3-A679-775E-EBADA9D2D5D5";
	setAttr ".t" -type "double3" 0 5 5.7931375494497503e-016 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "head_back" -p "head_back_zro";
	rename -uid "7B1C4517-4D3D-7939-4607-E3B3AC07EE39";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 7;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".dh" yes;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.5 0.5 0 ;
createNode nurbsCurve -n "head_backShape" -p "head_back";
	rename -uid "83744EF1-4FB1-CAF1-F49B-8295E51510C2";
	addAttr -s false -ci true -sn "curveConnectedTo" -ln "curveConnectedTo" -at "message";
	addAttr -s false -ci true -sn "curveConnectedLOC" -ln "curveConnectedLOC" -at "message";
	addAttr -s false -ci true -sn "curveConnectedOrgShape" -ln "curveConnectedOrgShape" 
		-at "message";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		0 -4.9995000928241744 1.2911737794200881e-008
		;
	setAttr ".ipo" yes;
createNode nurbsCurve -n "head_backShapeOriginal" -p "head_back";
	rename -uid "B9868FF1-43AA-5375-7F27-1B901287E32C";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		0 0 0
		;
createNode transform -n "head_pos" -p "hdl_grp";
	rename -uid "9433DD19-4D23-F860-81B8-EDB03CC0320E";
createNode transform -n "headEnd_zro" -p "head_pos";
	rename -uid "BE75BCC4-4870-D8AE-0F52-F5B67196A7FC";
	setAttr ".ove" yes;
	setAttr ".ovc" 5;
	setAttr ".t" -type "double3" 10 -1.9428902930940239e-015 0 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "headEnd_pos" -p "headEnd_zro";
	rename -uid "6ABFF026-4584-547A-DCA7-23B621B1ACAE";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 5;
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".dh" yes;
createNode nurbsCurve -n "headEnd_posShape" -p "headEnd_pos";
	rename -uid "D5B2FA92-4FDC-DDC3-41E7-74B6A8A6EB42";
	addAttr -s false -ci true -sn "curveConnectedTo" -ln "curveConnectedTo" -at "message";
	addAttr -s false -ci true -sn "curveConnectedLOC" -ln "curveConnectedLOC" -at "message";
	addAttr -s false -ci true -sn "curveConnectedOrgShape" -ln "curveConnectedOrgShape" 
		-at "message";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		-9.9990000999900008 1.7763568394002505e-015 1.2748000424233248e-017
		;
	setAttr ".ipo" yes;
createNode nurbsCurve -n "headEnd_posShapeOriginal" -p "headEnd_pos";
	rename -uid "10F73EF5-4B25-EE68-1607-6C9641ABEA18";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		0 0 0
		;
createNode transform -n "neck_rot" -p "head_pos";
	rename -uid "2B49813B-48CE-3FBB-9FB4-BCBA8374DC83";
	setAttr ".t" -type "double3" 4.2833456781465884e-008 1.2913029534544762e-008 -1.0649521640718244e-024 ;
	setAttr ".r" -type "double3" -179.99999999999994 1.4756782077829983e-014 158.19859071549109 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 1 ;
createNode transform -n "neck_zro" -p "neck_rot";
	rename -uid "D2478E46-4C46-0159-0CAC-ECA051FFC542";
	setAttr ".t" -type "double3" 5.3851648421085958 -8.9264071689854063e-009 2.1521856384598619e-015 ;
	setAttr ".r" -type "double3" 0 180 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "neck_pos" -p "neck_zro";
	rename -uid "A58119A1-4DC5-417A-0F8C-3981E64478BE";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 5;
	setAttr ".t" -type "double3" 0 0 -9.8607613152626476e-032 ;
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".dh" yes;
createNode nurbsCurve -n "neck_posShape" -p "neck_pos";
	rename -uid "304EB9C7-43F3-4237-03B0-B6B36EDADA14";
	addAttr -s false -ci true -sn "curveConnectedTo" -ln "curveConnectedTo" -at "message";
	addAttr -s false -ci true -sn "curveConnectedLOC" -ln "curveConnectedLOC" -at "message";
	addAttr -s false -ci true -sn "curveConnectedOrgShape" -ln "curveConnectedOrgShape" 
		-at "message";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 -3.944304526105059e-031 1.9721522630525295e-031
		5.3846263604064131 -5.8734978861302589e-008 1.2911739866000542e-008
		;
	setAttr ".ipo" yes;
createNode nurbsCurve -n "neck_posShapeOriginal" -p "neck_pos";
	rename -uid "3647BD77-4DC2-795A-3B81-CC816A519E06";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		0 0 0
		;
createNode transform -n "neck_aim_zro" -p "head_pos";
	rename -uid "01DCAAA0-406A-FB1B-8E47-33AA46724950";
	setAttr ".t" -type "double3" -7.3526454885435388 2.9410581954174213 -2.0395842750170898e-015 ;
	setAttr ".r" -type "double3" 0 0 -21.801409486351851 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "neck_aim" -p "neck_aim_zro";
	rename -uid "6BD77830-4D0A-07C3-33DB-249AD6B57012";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 4;
	setAttr -l on ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".dh" yes;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.5 0.5 0 ;
createNode nurbsCurve -n "neck_aimShape" -p "neck_aim";
	rename -uid "C0A24DD4-4EC0-A1A0-6767-32AD5C9EB9EA";
	addAttr -s false -ci true -sn "curveConnectedTo" -ln "curveConnectedTo" -at "message";
	addAttr -s false -ci true -sn "curveConnectedLOC" -ln "curveConnectedLOC" -at "message";
	addAttr -s false -ci true -sn "curveConnectedOrgShape" -ln "curveConnectedOrgShape" 
		-at "message";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		-4.4408920985006262e-016 6.9903150368647359e-018 9.8607613152626476e-031
		2.5336233753761452 -1.6773990750823028e-015 -1.1259008876881582e-016
		;
	setAttr ".ipo" yes;
createNode nurbsCurve -n "neck_aimShapeOriginal" -p "neck_aim";
	rename -uid "B56A9013-4C38-E93D-53C1-EE8F432C8DE2";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		0 0 0
		;
createNode transform -n "rig_grp" -p "root";
	rename -uid "4B46C056-423F-DB0E-2A40-7A8BD2577283";
	setAttr ".v" no;
createNode transform -n "calc_jointOrient_grp" -p "rig_grp";
	rename -uid "97750C2D-4E50-BCDB-DA5A-86BEEA5FB9E3";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".it" no;
createNode transform -n "constMe_to_parent" -p "calc_jointOrient_grp";
	rename -uid "EB8D7166-4C89-E101-2D0C-0580FA7614F8";
createNode transform -n "neck_jo" -p "constMe_to_parent";
	rename -uid "1968E281-4965-B2D6-87F6-F693FDBF92E6";
	setAttr ".t" -type "double3" -1.5543122267665994e-015 -3.5527136788005009e-015 
		-3.5527136788005009e-015 ;
	setAttr ".r" -type "double3" -89.999999999999972 -21.80140948635184 90 ;
createNode transform -n "head_jo" -p "neck_jo";
	rename -uid "BCBE6BC9-4C7B-1752-E46A-4482ECFCB047";
	setAttr ".t" -type "double3" 5.3851648071345082 6.8536815500708621e-016 2.3930795360932511e-016 ;
	setAttr ".r" -type "double3" 1.1756037443598253e-015 6.1044193165305992e-015 21.80140948635183 ;
createNode transform -n "const_grp" -p "rig_grp";
	rename -uid "15C4404F-42F1-936A-619F-318F2CA0C073";
	setAttr ".t" -type "double3" 8.8817841970012523e-016 -3.3355350494384766 -0.29590487480163574 ;
createNode transform -n "head_pos_locator1" -p "const_grp";
	rename -uid "14813830-46B1-2A46-B183-62B0F925793E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -5.9787339602818195e-016 3.3355350066050198 0.29590488771466528 ;
	setAttr ".r" -type "double3" 90 89.999999999999986 0 ;
createNode locator -n "head_pos_locatorShape1" -p "head_pos_locator1";
	rename -uid "A1DE8C37-4D6E-EF67-97F0-88A4114E06D5";
	setAttr -k off ".v" no;
createNode transform -n "neck_pos_locator1" -p "const_grp";
	rename -uid "1F958423-4A9F-499A-3904-A589217CB31E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -5.0000000000000044 5.3355350494384801 0.29590487480163358 ;
	setAttr ".r" -type "double3" 90 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
createNode locator -n "neck_pos_locatorShape1" -p "neck_pos_locator1";
	rename -uid "DDD9AD25-4D56-6370-9381-C590B3332439";
	setAttr -k off ".v" no;
createNode transform -n "head_pos_locator2" -p "const_grp";
	rename -uid "9BB750F1-4199-9B2F-4E05-499531C2BD14";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -5.9787339602818195e-016 3.3355350066050198 0.29590488771466528 ;
	setAttr ".r" -type "double3" 90.000000000000014 89.999999999999929 0 ;
createNode locator -n "head_pos_locatorShape2" -p "head_pos_locator2";
	rename -uid "D23C14A9-4AC7-7FBC-6D6C-A991FD8FFFB9";
	setAttr -k off ".v" no;
createNode transform -n "headEnd_pos_locator1" -p "const_grp";
	rename -uid "95D8C580-4863-CD85-AE00-3C976F1C1425";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 10 3.3355350494384748 0.29590487480163574 ;
	setAttr ".r" -type "double3" 89.999999999999986 89.999999999999957 0 ;
createNode locator -n "headEnd_pos_locatorShape1" -p "headEnd_pos_locator1";
	rename -uid "1643B7E5-4F2F-4C6F-5833-DCB95B69F656";
	setAttr -k off ".v" no;
createNode transform -n "rot_locator1" -p "const_grp";
	rename -uid "B352747D-43B3-813C-7A7E-8590097212E7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -8.8817841970012523e-016 3.3355350494384766 0.29590487480163574 ;
	setAttr ".r" -type "double3" 90 89.999999999999986 0 ;
createNode locator -n "rot_locatorShape1" -p "rot_locator1";
	rename -uid "F20AFE4C-4B03-D2B3-9E1B-9783D1F6D6B8";
	setAttr -k off ".v" no;
createNode transform -n "result_grp" -p "rig_grp";
	rename -uid "6361083F-4A6A-FD37-26D1-6BBED10F4411";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".it" no;
createNode joint -n "result_neck" -p "result_grp";
	rename -uid "A1FABE92-451F-5E55-C3D7-D69B4D25530F";
	setAttr ".t" -type "double3" -1.5543122267665994e-015 -3.5527136788005009e-015 
		-3.5527136788005009e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 7;
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode joint -n "result_head" -p "result_neck";
	rename -uid "123E86A0-4075-4E04-C426-378E76964341";
	setAttr ".t" -type "double3" 5.3851648071345082 6.8536815500708621e-016 2.3930795360932511e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 8;
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
createNode joint -n "result_headEnd" -p "result_head";
	rename -uid "AD114E3F-4F57-B15E-05B0-C9A178E2E3B3";
	setAttr ".t" -type "double3" 10 0 -4.234728858490911e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "HeadEnd";
	setAttr ".radi" 0.5;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 0 0 ;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "headEnd_pos.msg" "head_upShape.curveConnectedTo";
connectAttr "headEnd_pos_locator1.msg" "head_upShape.curveConnectedLOC";
connectAttr "head_pos_locator1.msg" "head_backShape.curveConnectedLOC";
connectAttr "head_pos.msg" "headEnd_posShape.curveConnectedTo";
connectAttr "rot_locator1.msg" "headEnd_posShape.curveConnectedLOC";
connectAttr "head_pos_locator2.msg" "neck_posShape.curveConnectedLOC";
connectAttr "neck_pos.msg" "neck_aimShape.curveConnectedTo";
connectAttr "neck_pos_locator1.msg" "neck_aimShape.curveConnectedLOC";
connectAttr "neck_jo.r" "result_neck.jo";
connectAttr "result_neck.s" "result_head.is";
connectAttr "head_jo.r" "result_head.jo";
connectAttr "result_head.s" "result_headEnd.is";
// End of head_template.ma
