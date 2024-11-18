import maya.utils
import noraMayaSetup

def create_nora_menu():
    nora = noraMayaSetup.NoraSMC()
    nora.add_menu()

print("maya.utils.executeDeferred(create_nora_menu)")
maya.utils.executeDeferred(create_nora_menu)