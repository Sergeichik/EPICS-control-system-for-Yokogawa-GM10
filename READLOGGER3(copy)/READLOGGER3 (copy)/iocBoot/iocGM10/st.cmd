#!../../bin/linux-x86_64/GM10

#- You may have to change GM10 to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/GM10.dbd"
GM10_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/GM10.db","user=paraffin")
dbLoadRecords("db/GM10.db", "user=paraffin")
cd "${TOP}/iocBoot/${IOC}"
iocInit
epicsThreadSleep 1
dbpf "IR:paraffin:GM10:channels.MODE" "EL"

## Start any sequence programs
#seq sncxxx,"user=paraffin"

