//Maya ASCII 2017 scene
//Name: head_joint.ma
//Last modified: Thu, Nov 03, 2016 12:34:33 PM
//Codeset: 949
requires maya "2017";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201608291545-1001872";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode joint -n "neck_jnt";
	rename -uid "ADA17E22-40C2-8CE1-EDBF-6A87C9944334";
	setAttr ".t" -type "double3" 0 -1.6644649933949811 -1.7040951122853374 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90 -21.801409486351844 90 ;
	setAttr ".typ" 7;
	setAttr ".radi" 0.72681886933454343;
createNode joint -n "head_jnt" -p "neck_jnt";
	rename -uid "174341A0-4CF5-418F-E458-B5BB8B461A9C";
	setAttr ".t" -type "double3" 5.3851648071345055 1.3322676295501878e-015 5.9787339602818175e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.0993518255460163e-016 -4.7249134173197779e-015 
		21.80140948635183 ;
	setAttr ".typ" 8;
	setAttr ".radi" 1.0172413793103448;
createNode joint -n "headEnd_jnt" -p "head_jnt";
	rename -uid "FC99268A-48A1-A43C-4515-C99CC15A5204";
	setAttr ".t" -type "double3" 11 1.9428902930940239e-015 9.0711825604275772e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "HeadEnd";
	setAttr ".radi" 1.0172413793103448;
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
connectAttr "neck_jnt.s" "head_jnt.is";
connectAttr "head_jnt.s" "headEnd_jnt.is";
// End of head_joint.ma
