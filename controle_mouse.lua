scriptId = 'com.gfdsantos.myotest1'
scriptTitle = "Teste 1"
scriptDetailsUrl = "" -- We don't have this until it's submitted to the Myo Market

function onPoseEdge(pose, edge)
    myo.debug("onPoseEdge: " .. pose .. ", " .. edge)
end

function activeAppName()
    return "Output Everything"
end

function onPeriodic()
	x, y, z = myo.getAccel()
	myo.debug("[" .. x .. ", " .. y .. ", " .. z .. "]")
	braco = myo.getArm()
	myo.debug("getArm: " .. braco)
end

function onActiveChange(isActive)
    myo.debug("onActiveChange")
end

myo.centerMousePosition()
myo.controlMouse(true)