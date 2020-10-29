import arcpy  
from arcpy import env
import glob
##Destination GDB  
GDBD=r"D:\HKU\t20201029a_jilin_building\test2\Derrick Ho/HKU_AOI18.gdb"
fp = r'D:\HKU\t20201029a_jilin_building\test2\Derrick Ho\Derrick Ho/'

GDBS = glob.glob(fp+'*.gdb')
GDBS2 = glob.glob(fp+'*/*.gdb')
GDBS3 = glob.glob(fp+'*/*/*.gdb')
print(GDBS)
print('\n')
print(GDBS2)
print('\n')
print(GDBS3)
GDBS = GDBS+GDBS2+GDBS3

if True:
    ##List of Origin GDB  
    #GDBS=[fp+"HKU_Job32/HKU_Job32.gdb",fp+"HKU_Job33/HKU_Job33.gdb",
    #      fp+"HKU_Job34/HKU_Job34.gdb",fp+"HKU_Job35/HKU_Job35.gdb",
    #      fp+"HKU_Job36/HKU_Job36.gdb"]  
    ##Set Environment  
    arcpy.env.workspace=GDBD  
    ##Get List of FDS  
    FDS=arcpy.ListDatasets()  
    ##Get List of Root Feature Classes  
    ROOTFCS=arcpy.ListFeatureClasses()  
      
    ##Append elements in Root Feature Classes  
    for fcr in ROOTFCS:  
        appendinput=[]  
        for FCI in GDBS:  
            appendinput.append(FCI+"/"+fcr)  
        ##print appendinput  
        arcpy.Append_management(appendinput,GDBD+'/'+fcr,"TEST")  
      
    ##Append elements of Feature Classes inside Feature Datasets  
    for FD in FDS:  
        for FC in arcpy.ListFeatureClasses("*","",FD):  
            appendinput2=[]  
            for FCI2 in GDBS:  
                    appendinput2.append(FCI2+"/"+FC)  
            ##print appendinput2  
            arcpy.Append_management(appendinput2,GDBD+'/'+FC,"TEST")  
