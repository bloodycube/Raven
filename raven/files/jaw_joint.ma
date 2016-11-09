//Maya ASCII 2017 scene
//Name: jaw_joint.ma
//Last modified: Wed, Nov 09, 2016 10:55:53 AM
//Codeset: 949
requires maya "2017";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201608291545-1001872";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode joint -n "jaw__SIDE__jnt";
	rename -uid "25ADC61D-4DF6-0701-4439-5097CDCC3C27";
	setAttr ".t" -type "double3" -1.341149131594612e-015 4.2300000526263046 2.42390488761861 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -89.999999999999986 0 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Jaw";
	setAttr ".radi" 0.5;
createNode joint -n "jawEnd__SIDE__jnt" -p "jaw__SIDE__jnt";
	rename -uid "CB8C2278-42D3-C8B4-5D82-CFBC19274FBA";
	setAttr ".t" -type "double3" 6.0399987292977606 -4.5351547767534228 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -36.901185656977269 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "JawEnd";
	setAttr ".radi" 0.5;
createNode joint -n "lowerTeeth__SIDE__jnt" -p "jaw__SIDE__jnt";
	rename -uid "B1AE21DE-4365-73CE-3680-298435C364A9";
	setAttr ".t" -type "double3" 3.9308021568236264 -0.63924488819629754 -4.6833571964424879e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode joint -n "upperTeeth__SIDE__jnt";
	rename -uid "6C545538-4D95-1409-1AF2-159A2B9E9F24";
	setAttr ".t" -type "double3" 0 4.966671755944283 6.3856897422026559 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -90 0 ;
	setAttr ".radi" 0.5;
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
connectAttr "jaw__SIDE__jnt.s" "jawEnd__SIDE__jnt.is";
connectAttr "jaw__SIDE__jnt.s" "lowerTeeth__SIDE__jnt.is";
// End of jaw_joint.ma
