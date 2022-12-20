## Simple customization function which add cms.ignore in front of all L1 seed. Ie. replace of "process.hltL1S...." with "cms.ignore(process.hltL1S....)"

def ignoreAllL1Seeds(process):
    import FWCore.ParameterSet.Config as cms
    l1seeds = []
    for moduleName in process.filters_():
        if process.filters_()[moduleName].type_() == 'HLTL1TSeed':
            l1seeds.append(moduleName)

    for pathName in process.paths_():
        pathPython = process.paths_()[pathName].dumpPythonNoNewline()
        for l1seed in l1seeds:
            if l1seed in pathPython:
                pathPython = pathPython.replace("+process.%s+"%l1seed,"+cms.ignore(process.%s)+"%l1seed)
        setattr(process, pathName, eval(pathPython))
