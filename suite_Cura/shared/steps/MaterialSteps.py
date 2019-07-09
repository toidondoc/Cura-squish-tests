from PageObjects.MaterialsPage import Materials
from PageObjects.CuraPage import Cura
from PageObjects.PreferencesPage import Preferences


materials = Materials()
cura = Cura()

@When("I activate material '|any|'")
def step(context, material_type):
    materials.navigateToMaterialsPreferences("nl")
    materials.activateMaterial(material_type)
    cura.pressCloseButton()


@Then("Extruder one makes use of material '|any|'")
def step(context, expected_material):
    actual_material = materials.getExtruderOneMaterial()
    test.compare(expected_material, actual_material.text, f"Actual material: {actual_material.text}" )

@Then("the material '|any|' has been added")
def step(context, material_name):
    materials.verifyMaterialPresent(material_name)

@Then("the material '|any|' has not been added")
def step(context, material_name):
    materials.verifyMaterialNotPresent(material_name)

@Step("I select |word| material")
def step(context, action):
    preferences.selectPreferencesMenu(action)
    
@Step("I select '|any|'")
def step(context, action):
    materials.unlinkMaterial(action)

@Step("I change the material name to '|any|'")
def step(context, new_name):
    materials.renameMaterial(new_name)

@Step("I change the material property '|word|' to '|any|'")
def step(context, property_name, property_value):
    materials.setProperty(property_name, property_value)

@Step("I confirm changing the diameter")
def step(context):
    materials.confirmDialog()