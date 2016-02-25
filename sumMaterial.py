from __future__ import division

theToroid={'toroidMagnet':9*4,'theToroidCenter':1}
theToroidCenter={'solenoidMagnet':1,'solenoidHub':17,
            'hysteresisRod':6*4+4*4,'centralPermanentMagnet':5*4,'auxiliaryPermanentMagnet':7*4,
            'ferromagneticBase':5*4*2,'magneticLinkage':7*4*2,
            'vanDeGraaffGenerator':1}
thePlasmaGen={'vanDeGraaffGenerator':2,
              'preheaterUnitHousingCorner':8+4,'preheaterUnitHousingEdge':3*12+4,'preheaterUnitHousingFace':8*6,
              'thermalInsulationCore':9+5+8+8, 'liquidPipe':4,'laserConcentrationLens':2,'hydrogenPreheater':1,
              'heatRay':1
              }
theTritium={}
theDeuterium={}
thePlasma={'fusionPlasmaInjector':1,'plasmaInjectorInductionCoil':3,'magneticContainmentPipe':10,
            'plasmaInjectorBase':9,'plasmaInjectorLowerCorner':9*2,'plasmaInjectorColumnPiece':3*2+1*2,
            'plasmaInjectorTop':9,'plasmaInjectorUpperCorner':9*2,
            'plasmaInjectorHysteresisCore':11,'plasmaInjectorSidePanel':16,
            'thePlasmaGen':1}
theAbsorber={'neutronAbsorber':1,'liquidPipe':1,'steamBoiler':1,'steamLine':1}
theTurbine={'turbine':5}
theReactor={'theToroid':1,'thePlasma':1,'theAbsorber':1,'fusionPlasmaInjector':3}

plasmaInjectorLowerCorner={'thermalInsulationCore':1,'hysteresisPlate':1,'ferromagneticPlate':7}
plasmaInjectorColumnPiece={'thermalInsulationCore':2,'ferromagneticPlate':6,'hysteresisPlate':1}
plasmaInjectorTop={'thermalInsulationCore':3,'hysteresisPlate':3,'ferromagneticPlate':3}
plasmaInjectorUpperCorner={'thermalInsulationCore':1,'hysteresisPlate':1,'ferromagneticPlate':7}
plasmaInjectorHysteresisCore={'thermalInsulationCore':1,'hysteresisPlate':4,'ferromagneticPlate':1}
plasmaInjectorSidePanel={'thermalInsulationCore':4,'ferromagneticPlate':4,'hysteresisPlate':1}
plasmaInjectorBase={'thermalInsulationCore':3,'hysteresisPlate':3,'ferromagneticPlate':3}
plasmaInjectorInductionCoil={'spatialStorageCell128':4,'goldWiring':1,'ferromagneticPlate':4}
spatialStorageCell128={'spatialComponent128':1}
spatialComponent128={'spatialComponent16':4,'engineeringProcessor':1}
spatialComponent16={'spatialComponent2':4,'engineeringProcessor':1}
spatialComponent2={'fluixPeral':4,'engineeringProcessor':1}
fusionPlasmaInjector={'magneticContainmentPipe':4,'ferromagneticPlate':4}
heatRay={'obsidian':3,'basePanel':2,'heatRayCore':1,'lens':1,'heatRayBarrel':1,'powerModule':1}
laserConcentrationLens={'ferromagneticIngot':1,'ferromagneticPlate':4,'quantumSolarPanel':1,'celestialMirror':1,'galgadorianDrill':1,'torcherino':1}
hydrogenPreheater={'ferromagneticIngot':4,'blastGlass':4}
blastGlass={'obsidian':1}
preheaterUnitHousingFace={'HSLASteelIngot':8,'thermalInsulationCore':4}
preheaterUnitHousingEdge={'HSLASteelIngot':5,'thermalInsulationCore':4}
preheaterUnitHousingCorner={'HSLASteelIngot':5,'thermalInsulationCore':4}
thermalInsulationCore={'wool':8,'HSLASteelIngot':1}
magneticLinkage={'hysteresisPlate':4,'hyperenergeticNitor':2,'provenFrame':2,'extendedDrawbridge':1}
ferromagneticBase={'ferromagneticPlate':4,'etherealSlate':2,'octupleCompressedCobblestone':2,'mimikineticUpheaver':1}
auxiliaryPermanentMagnet={'ferromagneticPlate':6,'permanentMagnet4096':3}
centralPermanentMagnet={'ferromagneticPlate':6,'permanentMagnet16384':3}
permanentMagnet16384={'permanentMagnet4096':4/2}
permanentMagnet4096={'permanentMagnet1024':4/2}
permanentMagnet1024={'permanentMagnet256':4/2}
permanentMagnet256={'permanentMagnet64':4/2}
permanentMagnet64={'permanentMagnet16':4/2}
permanentMagnet16={'permanentMagnet4':4/2}
permanentMagnet4={'permanentMagnet1':4/2}
permanentMagnet1={'lodestone':4/2}
hysteresisRod={'hysteresisPlate':2,'ferromagneticPlate':2,'alchemite':2,'bootleoEnchanting':2,'fireWaterBucket':1}
solenoidHub={'hysteresisPlate':2,'ferromagneticPlate':2,'xeon':1,'redstoneCrystal':2,'osmiumShard':2}
redstoneCrystal={'redstone':9}
solenoidMagnet={'HSLASteelIngot':2,'basePanel':1,'ferromagneticPlate':2,'magneticCore':1,'ferromagneticIngot':2,'gearUnit16':1}
toroidMagnet={'magneticCore':4,'coolantPack':4,'hysteresisRing':1}
magneticCore={'ferromagneticPlate':8}
ferromagneticPlate={'ferromagneticIngot':6/32,'timespace':1/32,'matter':1/32,'dragon':1/32}
coolantPack={'HSLASteelIngot':6,'liquidPipe':1,'glassPane':1}
hysteresisRing={'hysteresisPlate':8}
hysteresisPlate={'ferromagneticIngot':6/8,'tech':1/8,'magic':1/8,'dragon':1/8}
ferromagneticIngot={'HSLASteelIngot':1,'ironIngot':1,'lodestone':1}
basePanel={'HSLASteelIngot':1}
goldenEgg={'goldenApple':2,'cake':1,'goldOreberryBush':2,'cratedPotashApple':4}
goldenApple2={'goldenApple':1,'goldenEgg':8}
goldenHead2={'goldenHead':1,'cratedPotashApple':4,'goldenEgg':4}
creativeToolModifier={'goldenHead2':1,'goldenApple2':8}
dragon={'creativeToolModifier':1}


Result={}
def sumMaterial(sth,num):
    for name,count in globals()[sth].items():
        if name in globals():
            sumMaterial(name,num*count)
        else:
            if name in Result:
                Result[name]+=(count*num)
            else:
                Result[name]=(count*num)

if __name__ == '__main__':
    needSum={'theToroidCenter':1}
    for k,v in needSum.items():
        print ''.ljust(16,'=')
        print 'to make',v,k,', you need'
        print ''.ljust(8,'-')
        sumMaterial(k,v)
        for (name,count) in sorted(Result.items()):
            print name,'\t',count
