#################################################################
# Drought Monitor V2
# Written by: Nathaniel W. Chaney
# Date: 12 July 2013
# Location: Princeton University
# Contact: nchaney@princeton.edu
# Purpose: Main driver of the drought monitor
##################################################################

import MASTER_LIBRARY as ml
import datetime
import numpy as np
import grads
import os
import dateutil.relativedelta as relativedelta
import time

def Download_and_Process(date):

 #################################################
 #DOWNLOAD AND PREPROCESS ALL THE REQUIRED DATA
 #################################################

 #Reprocess available pgf data (historical)
 #ml.Reprocess_PGF(date,dims)

 #Download and process the gfs final analysis data
 #ml.Download_and_Process_NCEP_FNL_Analysis(date,dims,idate,fdate,False)

 #Download and process the 3b42rt precipitation data
 ml.Download_and_Process_3b42RT(date,dims,False)

 #Download gfs forecast
 #ml.Download_and_Process_GFS_forecast(date,dims,False)

 #Download and process modis NDVI
 #ml.Download_and_Process_NDVI(date,dims,False)

 #Download and process the seasonal forecast
 ml.Download_and_Process_Seasonal_Forecast(date,False)

 #Download and process the gfs analysis data
 #ml.Download_and_Process_GFS_Analysis(date,dims,False)

 return

def BiasCorrect(date):

 #################################################
 #BIAS CORRECT THE DOWNLOADED DATA
 #################################################

 #Regrid and downscale 3b42rt (ensure it complies with the pgf grid)
 ml.Regrid_and_Output_3B42rt(date,dims,False)

 #Bias correct the 3b42rt precipitation product
 ml.BiasCorrect_and_Output_Forcing_3B42RT_Daily(date,dims,False)

 #Bias correct the gfs final analysis product
 #ml.BiasCorrect_and_Output_Forcing_FNL_Daily(date,dims)

 #Bias correct the gfs forecast
 ml.BiasCorrect_and_Output_Forcing_GFS_Daily(date,dims,False)

 #Bias correct the seasonal forecast
 
 #Compute different moving averages of the ndvi product
 #ml.Compute_NDVI_moving_average(date,dims,False)

 #Bias correct the gfs analysis product
 ml.BiasCorrect_and_Output_GFSANL_Daily(date,dims,False)

 return

def Compute_Indices(date):

 #################################################
 #COMPUTE INDICES
 #################################################

 ml.Calculate_and_Output_SPI(date,dims,'monitor',date,False)

 #ml.Calculate_and_Output_NDVI_Percentiles(date,dims)

 ml.Calculate_and_Output_SM_Percentiles(date,dims,'monitor',date,True)

 #ml.BiasCorrect_and_Compute_Seasonal_Forecast_Products(date,dims,False)

 ml.Calculate_and_Output_Streamflow_Percentiles(date,dims,False,'monitor',date)

 return

def Compute_Forecast_Indices(date,idate):

 ml.print_info_to_command_line("Computing forecast indices for %d/%d/%d" % (date.day,date.month,date.year))

 ml.Calculate_and_Output_Streamflow_Percentiles(date,dims,True,'forecast',idate)

 ml.Calculate_and_Output_SM_Percentiles(date,dims,'forecast',idate,True)

 ml.Calculate_and_Output_SPI(date,dims,'forecast',idate,True)
 
 ml.BiasCorrect_and_Compute_Seasonal_Forecast_Products(date,dims,False)

 return

def Compute_Averages(date):

 #################################################
 #COMPUTE MONTHLY AND ANNUAL PRODUCTS
 #################################################

 #ml.Compute_Avarages_Routing(date,dims,dt)
 Averages_Reprocess_Flag = False#True
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'PGF',"../DATA/PGF/DAILY/pgf_daily_0.25deg.ctl","xdfopen",Averages_Reprocess_Flag)
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'3B42RT_BC',"../DATA/3B42RT_BC/DAILY/3B42RT_daily_0.25deg.ctl","xdfopen",Averages_Reprocess_Flag)
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'GFS_ANL_BC',"../DATA/GFS_ANL_BC/DAILY/gfsanl_daily_0.25deg.ctl","xdfopen",Averages_Reprocess_Flag)
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'VIC_PGF',"../DATA/VIC_PGF/DAILY/vic_daily_0.25deg.ctl","open",Averages_Reprocess_Flag)
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'VIC_3B42RT',"../DATA/VIC_3B42RT/DAILY/vic_daily_0.25deg.ctl","open",Averages_Reprocess_Flag)
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'ROUTING_VIC_PGF',"../DATA/ROUTING_VIC_PGF/DAILY/Streamflow.ctl","open",Averages_Reprocess_Flag)
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'ROUTING_VIC_3B42RT',"../DATA/ROUTING_VIC_3B42RT/DAILY/Streamflow.ctl","open",Averages_Reprocess_Flag)
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'MOD09_NDVI_MA',"../DATA/MOD09_NDVI_MA/DAILY/MOD09CMG_daily_0.25deg.ctl","xdfopen",Averages_Reprocess_Flag)
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'VIC_DERIVED',"../DATA/VIC_DERIVED/DAILY/vic_derived_daily_0.25deg.ctl","xdfopen",Averages_Reprocess_Flag)
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'ROUTING_VIC_DERIVED',"../DATA/ROUTING_VIC_DERIVED/DAILY/routing_vic_derived_daily_0.25deg.ctl","xdfopen",Averages_Reprocess_Flag)
 #ml.Compute_Monthly_Yearly_Averages(date,dims,dt,'SPI',"../DATA/SPI/DAILY/SPI_daily_0.25deg.ctl","xdfopen",Averages_Reprocess_Flag)

 return

dims = {}
dims['minlat'] = -34.875000 #-89.8750
dims['minlon'] = -18.875000 #0.1250
dims['nlat'] = 292 #720
dims['nlon'] = 296 #1440
dims['res'] = 0.250
dims['maxlat'] = dims['minlat'] + dims['res']*(dims['nlat']-1)
dims['maxlon'] = dims['minlon'] + dims['res']*(dims['nlon']-1)
dt = datetime.timedelta(days=1)
date = datetime.datetime.today()
idate = datetime.datetime(date.year,date.month,date.day) - 6*dt
idate = datetime.datetime(2013,8,31)
fdate = datetime.datetime(2013,8,31)
dates = []
#while date <= fdate:
# dates.append(date)
# date = date + dt

#Download and bias correct data
date = idate
while date <= fdate:
 #Download_and_Process(date)
 BiasCorrect(date)
 date = date + dt

#Run VIC
#ml.Run_VIC(idate,fdate,dims,'3b42rt')
#ml.Run_VIC(idate,fdate,dims,'pgf')
#ml.Run_VIC(idate,fdate,dims,'gfs_forecast')

#Run the Routing model
#ml.Run_VDSC(idate,fdate+datetime.timedelta(days=7),dims,'pgf')
#ml.Run_VDSC(idate,fdate,dims,'3b42rt')
#ml.Run_VDSC(idate,fdate,dims,'gfs_forecast')

#Compute Monitor Indices
date = idate
while date <= fdate:
 #print date
 #Compute_Indices(date) 
 date = date + dt

#Compute Forecast Indices
date = fdate + datetime.timedelta(days=1)
while date <= fdate + 7*dt:
 #Compute_Forecast_Indices(date,fdate + dt)
 date = date + dt

#Compute Averages
date = idate
while date <= fdate:
 #Compute_Averages(date)
 date = date + dt

#Finalize GFS forecast
ml.Finalize_GFS_forecast(fdate+datetime.timedelta(days=1),dims)

#ml.Finalize_NCEP_FNL_Connection()

#################################################
#RUN THE VIC MODEL
#################################################

#Run the model

#Run VIC
#ml.Run_VIC(idate,fdate,dims,'3b42rt')
#ml.Run_VIC(idate,fdate,dims,'pgf')
#ml.Run_VIC(idate,fdate,dims,'gfsanl')
#ml.Run_VIC(idate,fdate,dims,'gfs_forecast')

 
#################################################
#RUN ROUTING MODEL
#################################################

#Run the VDSC model (Josh Roundy)

#ml.Run_VDSC(idate,fdate+datetime.timedelta(days=7),dims,'3b42rt')
