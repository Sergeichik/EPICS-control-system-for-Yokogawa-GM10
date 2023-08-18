TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = GM10
# GM10.dbd will be created and installed
DBD += GM10.dbd

# GM10.dbd will be made up from these files:
GM10_DBD += base.dbd

# Include dbd files from all support applications:
#GM10_DBD += xxx.dbd
GM10_DBD += netDev.dbd
# Add all the support libraries needed by this IOC
#GM10_LIBS += xxx
GM10_LIBS += asyn
GM10_LIBS += netDev
# GM10_registerRecordDeviceDriver.cpp derives from GM10.dbd
GM10_SRCS += GM10_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
GM10_SRCS_DEFAULT += GM10Main.cpp
GM10_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#GM10_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
GM10_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE


