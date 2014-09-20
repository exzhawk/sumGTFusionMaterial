from __future__ import division

fusionAll = {'fusionReactor': 1, 'fusionPeriphral': 1, 'plasmaGenerator': 16}
plasmaGenerator = {'tungstensteel': 5, 'HVtransformer': 1, 'energyFlowCircuit': 2, 'generator': 1}
generator = {'reBattery': 1, 'furnace': 1, 'steelMachineHull': 1}
fusionPeriphral = {'industrialElectrolyzer': 7, 'MVTransformer': 7, 'industrialCentrifuge': 15, 'LVTransformer': 15,
                   'dragonEggEnergySiphon': 6}
industrialElectrolyzer = {'steelPlate': 4, 'advancedCircuit': 2, 'automaticExtractor': 1, 'electrolyzer': 1,
                          'magnetizer': 1}
automaticExtractor = {'treetap': 4, 'steelMachineHull': 1, 'electronicCircuit': 1}
electrolyzer = {'cuCable': 4, 'electronicCircuit': 1, 'cell': 2, 'basicMachineCasing': 1}
basicMachineCasing = {'fePlate': 8}
magnetizer = {'redstone': 6, 'feFence': 2, 'basicMachineCasing': 1}
MVTransformer = {'cuCable': 2, 'basicMachineCasing': 1}
LVTransformer = {'woodPlank': 6, 'snCable': 2, 'coil': 1}
snCable = {'uninsulatedSnCable': 1, 'rubber': 1}
coil = {'fe': 1, 'uninsulatedCuCable': 8}
industrialCentrifuge = {'stainlessSteelPlate': 4, 'advancedCircuit': 2, 'steelMachineHull': 2, 'automaticExtractor': 1}
stainlessSteelPlate = {'stainlessSteel': 1}
stainlessSteel = {'fe': 6 / 9, 'ni': 1 / 9, 'mn': 1 / 9, 'cr': 1 / 9}
dragonEggEnergySiphon = {'energyFlowCircuit': 4, 'iridiumReinforcedPlate': 2, 'lapotronicEnergyOrb': 1, 'teleporter': 1,
                         'supercondensator': 1}
teleporter = {'advancedCircuit': 4, 'frequencyTransmitter': 1, 'advancedMachineCasing_ic2': 1, 'diamond': 1,
              'glassFibreCable': 2}
frequencyTransmitter = {'electronicCircuit': 1, 'cuCable': 1}
glassFibreCable = {'glass': 6, 'agDust': 1, 'energiumDust': 2}
advancedMachineCasing_ic2 = {'cPlate': 2, 'advancedAlloy': 2, 'basicMachineCasing': 1}

fusionReactor = {'fusionControlComputer': 1, 'fusionMaterialInjector': 2, 'fusionMaterialExtractor': 1,
                 'fusionEnergyInjector': 4, 'fusionCoils': 32, 'advancedMachineCasing': 120}
fusionControlComputer = {'energyFlowCircuit': 6, 'computerCube': 2, 'fusionCoils': 1}
energyFlowCircuit = {'processorCircuitBoard': 1, 'lapotronCrystal': 1}
processooard = {'ptPlate': 1, 'advancedCircuit': 1}
ptPlate = {'pt': 1}
#advancedCircuit = {'advancedCircuitBoard': 1, 'advancedCircuitParts': 2}
advancedCircuitBoard = {'agauPlate': 2, 'electronicCircuit': 1}
agauPlate = {'agau': 1}
electronicCircuit = {'basicCircuitBoard': 1, 'cuCable': 3}
basicCircuitBoard = {'fePlate': 0.5, 'agauPlate': 1}
basicCircuitBoard = {'fePlate': 1, 'redAlloyPlate': 2}
fePlate = {'fe': 1}
redAlloyPlate = {'redAlloy': 1}
redAlloy = {'cu': 1, 'redstone': 4}
cuCable = {'uninsulatedCuCable': 1, 'rubber': 1}
uninsulatedCuCable = {'cu': 1 / 3}
advancedCircuitParts = {'lapizLazuliDust': 1 / 2, 'glowstoneDust': 1 / 2}
lapotronCrystal = {'energyCrystal': 1, 'advancedCircuit': 2, 'lapizLazuliDust ': 6}
energyCrystal = {'energiumDust': 9}
energiumDust = {'redstone': 5 / 9, 'rubyDust': 4 / 9}
computerCube = {'dataOrb': 2, 'energyFlowCircuit': 2, 'steelMachineHull': 1, 'computerMonitor': 4}
dataOrb = {'dataControlCircuit': 1, 'dataStorageCircuit': 8}
dataControlCircuit = {'processorCircuitBoard': 1, 'dataStorageCircuit': 1}
dataStorageCircuit = {'emeraldPlate': 2, 'advancedCircuit': 1 / 4}
emeraldPlate = {'emerald': 1}
steelMachineHull = {'steelPlate': 6, 'machineParts': 1}
steelPlate = {'steel': 1}
steel = {'fe': 1, 'coalDust': 2}
coalDust = {'coal': 1}
machineParts = {'fePlate': 2, 'electronicCircuit': 1}
computerMonitor = {'alPlate': 4, 'glassPane': 1, 'glowstoneDust': 1, 'lapizLazuliDust': 1, 'roseRed': 1, 'limeDye': 1}
alPlate = {'al': 1}
glassPane = {'glass': 6 / 16}
#glass = {'sand': 1}
roseRed = {'rose': 1 / 3}
limeDye = {'cactusGreen': 1 / 2, 'boneMeal': 1 / 2}
cactusGreen = {'cactus': 1}
#boneMeal = {'bone': 1 / 7, 'woodAsh': 8 / 7}
fusionCoils = {'energyFlowCircuit': 4, 'superconductor': 1, 'nichromeHeatingCoil': 2, 'highlyAdvancedMachineblock': 1,
               'iridiumNeutronReflector': 1}
superconductor = {'c60kCoolantCell': 3, 'wPlate': 2, 'iridiumReinforcedPlate': 1, 'energyFlowCircuit': 3}
c60kCoolantCell = {'c30kCoolantCell': 2, 'snPlate': 6, 'fePlate': 1}
c30kCoolantCell = {'snPlate': 6, 'c10kCoolantCell': 3}
c10kCoolantCell = {'snPlate': 4, 'waterCell': 1}
snPlate = {'sn': 1}
wPlate = {'w': 1}
#iridiumReinforcedPlate = {'iridiumAlloy': 1, 'industrialTNT': 8}
iridiumAlloy = {'irPlate': 4, 'advancedAlloy': 4, 'diamond': 1}
irPlate = {'ir': 1}
advancedAlloy = {'mixedMetal': 1}
mixedMetal = {'fePlate': 3/2, 'bronzePlate': 3/2, 'snPlate': 3/2}
bronzePlate = {'bronze': 1}
#bronze = {'cu': 3 / 4, 'sn': 1 / 4}
industrialTNT = {'flintDust': 1, 'tnt': 3}
flintDust = {'tinyFlintDust': 9}
tinyFlintDust = {'flint': 1 / 4.4}
tnt = {'gunpowder': 4, 'sand': 4}
gunpowder = {'netherrack': 1}
nichromeHeatingCoil = {'nichrome': 5}
nichrome = {'cr': 1 / 5, 'ni': 4 / 5}
highlyAdvancedMachineblock = {'steelMachineHull': 1, 'crPlate': 4, 'tiPlate': 4}
crPlate = {'cr': 1}
tiPlate = {'ti': 1}
iridiumNeutronReflector = {'thickNeutronReflector': 8, 'iridiumReinforcedPlate': 1}
thickNeutronReflector = {'neutronReflector': 4, 'beCell': 1}
neutronReflector = {'snDust': 4, 'coalDust': 4, 'cuPlate': 1}
snDust = {'sn': 1}
cuPlate = {'cu': 1}
beCell = {'beDust': 1, 'cell': 1}
fusionMaterialInjector = {'pump': 4, 'chest': 1, 'energyFlowCircuit': 3, 'highlyAdvancedMachineblock': 1}
pump = {'tank': 1, 'miningWell': 1}
tank = {'glass': 8}
miningWell = {'redstone': 1, 'fe': 6, 'feGear': 1, 'fePickaxe': 1}
feGear = {'fe': 4, 'stoneGear': 1}
fePickaxe = {'fe': 3}
fusionMaterialExtractor = {'pump': 4, 'chest': 1, 'energyFlowCircuit': 3, 'highlyAdvancedMachineblock': 1}
pump = {'tank': 1, 'miningWell': 1}
fusionEnergyInjector = {'superconductor': 4, 'energyFlowCircuit': 4, 'supercondensator': 1}
supercondensator = {'energyFlowCircuit': 4, 'superconductor': 2, 'lapotronicEnergyOrb': 2,
                    'highlyAdvancedMachineblock': 1}
lapotronicEnergyOrb = {'lapotronCrystal': 8, 'iridiumReinforcedPlate': 1}
advancedMachineCasing = {'crPlate': 6 / 4, 'dataControlCircuit': 1 / 2, 'highlyAdvancedMachineblock': 1 / 4}

Result = {}

digSpell = {'spellAugmenter': 6, 'spellEmpowerer': 6, 'windGenerator': 1, 'environmentalModifier': 2, 'earthFormer': 1,
            'particleGenrator': 1}
#spellAugmenter={'obsidianBrace':4,'imbuedRunicPlate':2,'inputSpellCable':1,'outputSpellCable':1,'potencyCore':1}
#imbuedRunicPlate={'runicPlate':2,'incendium':1,'magicales':1,'aquasalus':1}
#runicPlate={'crackedRunicPlate':1,'terrae':1}
#crackedRunicPlate={'imbuedSlate':1,'concentratedCatalyst':1/2}
#concentratedCatalyst={'strengthenedCatalyst':1,'goldNugget':1,'fracturedBone':1}
#fracturedBone={'bone':1,'gunpowder':1/4}
#incendium={'lavaBucket':1,'netherrack':1,'simpleCatalyst':1,'blazePowder':2}
#magicales={'redstone':1,'simpleCatalyst':1,'gunpowder':1,'glowstoneDust':2}
#aquasalus={'inkSac':1,'simpleCatalyst':1,'waterBottle':3}
#potencyCore={'potentia':4,'emptyCore':1}
#potentia={'lapiz':2,'glowstoneDust':1,'quartz':1,'strengthenedCatalyst':1}
#spellEmpowerer={'obsidianBrace':4,'imbuedRunicPlate':2,'inputSpellCable':1,'outputSpellCable':1,'powerCore':1}
#obsidianBrace={'stoneBrace':1}
#powerCore={'virtus':4,'emptyCore':1}
#virtus={'coal':1,'redstone':2,'gunpowder':1,'strengthenedCatalyst':1}
#inputSpellCable={'imbuedSlate':1,'simpleCatalyst':1,'blankSlate':1}
#outputSpellCable={'simpleCatalyst':1}
#windGenerator={'stoneBrace':4,'inputSpellCable':1,'outputSpellCable':1,'gustyCore':1}
#gustyCore={'aether':4,'emptyCore':1}
#aether={'feather':2,'ghastTear':1,'glowstoneDust':1,'simpleCatalyst':1}
#environmentalModifier={'stoneBrace':4,'inputSpellCable':1,'outputSpellCable':1,'environmentalCore':1}
#environmentalCore={'orbisTerrae':4,'emptyCore':1}
#orbisTerrae={'strengthenedCatalyst':1,'netherrack':1,'sand':1,'gunpowder':1,'terrae':1}
#strengthenedCatalyst={'simpleCatalyst':1,'netherWart':1/2,'boneMeal':1/2}
#terrae={'sand':1,'dirt':1,'obsidian':2,'simpleCatalyst':1}
#earthFormer={'stoneBrace':4,'inputSpellCable':1,'outputSpellCable':1,'earthenCore':1}
#earthenCore={'terrae':4,'emptyCore':1}
#particleGenrator={'stoneBrace':2,'paradigmPlate':1,'outputSpellCable':1,'projectileCore':1}
#projectileCore={'magicales':4,'emptyCore':1}

#iridiumReinforcedPlate={'iridiumAlloy':1}
sunnariumAlloy={'iridiumReinforcedPlate':8,'sunnarium':1}
#sunnarium={'glowstone':1}
enrichedSunnariumAlloy={'sunnariumAlloy':1,'enrichedSunnarium':4}
enrichedSunnarium={'sunnarium':1,'irradiantUranium':8}
irradiantUranium={'uraniumIngot':1,'glowstoneDust':4}
ultimateHybridSolarPanel={'advancedSolarPanel':1,'coalChunk':3,'enrichedSunnariumAlloy':2}
quantumSolarPanel={'ultimateHybridSolarPanel':8,'quantumCore':1}
quantumCore={'enrichedSunnariumAlloy':4,'netherStar':4}


forceFieldEmitter={'solenoid':4,'enderPearl':4,'advancedCircuit':1}
solenoid={'fe':3,'wiring':6}
#wiring={'agCable':1, 'redstone':1/2}
#agCable={'ag':1/4}
turbine={'turbineGlass':4*7*12+2*7*7,'turbineHousing':4*14+8*7,'turbineController':1,'turbineFluidPort':2,'turbinePowerPort':1,'turbineRotorBearing':1,'turbineRotorBlade':84,'turbineRotorShaft':12}
#turbineController={'turbineHousing':4,'blutoniumIngot':2}
#turbineGlass={'turbineHousing':1,'glass':2}
#turbineFluidPort={'turbineHousing':4,'bucket':1,'piston':1,'fe':2}
#turbinePowerPort={'turbineHousing':4,'redstone':4}
#turbineRotorBearing={'turbineHousing':4,'turbineRotorShaft':2}
#turbineRotorBlade={'cyaniteIngot':1,'fe':2}
#turbineRotorShaft={'cyaniteIngot':1,'fe':2}
#turbineHousing={'fe':4,'graphiteBar':2,'quartz':2,'cyaniteIngot':1}
ME16MStorage={'quartzGlass':2,'fluixDust':3,'ME16MComponent':1,'diamond':3}
ME16MComponent={'glowstoneDust':4,'engineeringProcessor':1,'logicProcessor':1,'ME4MComponent':3}
ME4MComponent={'glowstoneDust':4,'engineeringProcessor':1,'logicProcessor':1,'ME1MComponent':3}
ME1MComponent={'glowstoneDust':4,'engineeringProcessor':1,'logicProcessor':1,'ME256kComponent':3}
ME256kComponent={'glowstoneDust':4,'engineeringProcessor':1,'logicProcessor':1,'ME64kComponent':3}
ME64kComponent={'glowstoneDust':4,'engineeringProcessor':1,'quartzGlass':1,'ME16kComponent':3}
ME16kComponent={'glowstoneDust':4,'engineeringProcessor':1,'quartzGlass':1,'ME4kComponent':3}
ME16kComponent={'redstone':4,'calculationProcessor':1,'quartzGlass':1,'ME1kComponent':3}
ME1kComponent={'redstone':4,'pureCertusQuartz':4,'logicProcessor':1}
quartzGlass={'glass':1,'quartzDust':4/5}
fluixDust={'fluixCrystal':1}
engineeringProcessor={'diamond':1,'redstone':1,'si':1}
logicProcessor={'au':1,'redstone':1,'si':1}
calculationProcessor={'pureCertusQuartz':1,'redstone':1,'si':1}



def sumMaterial(sth, num):
    for name, count in globals()[sth].items():
        if name in globals():
            sumMaterial(name, num * count)
        else:
            if name in Result:
                Result[name] += (count * num)
            else:
                Result[name] = (count * num)


needSum = {'quantumSolarPanel': 1}
for k, v in needSum.items():
    print ''.ljust(16, '=')
    print 'to make', v, k, ', you need'
    print ''.ljust(8, '-')
    sumMaterial(k, v)
    for (name, count) in sorted(Result.items()):
        print name, '\t', count
