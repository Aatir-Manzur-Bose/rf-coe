import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from rfcoe.classes import attenuator
from rfcoe.classes import codecomparator 

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post('/disable')
async def disable_cat(request: Request):
    da = await request.form()
    da = jsonable_encoder(da)
    print(da)
    print(da['startAttn'])

    cmdStr = ("python attenuator.py "
              "-i "
              "{} "
              "-a "
              "{} "
              "-s "
              "{} "
              "-e "
              "{}"
              "-w "
              "{} "
              "-d "
              "{} "
              "-o "
              "{} "
              "-k "
              "{} "
              "-p "
              "{} "
              "-b "
              "{}"
              "-B 1"
              ).format(da['attnId'],
                       da['attn'],
                       da['startAttn'],
                       da['endAttn'],
                       da['dwellTime'],
                       da['idleTime'],
                       da['holdTime'],
                       da['stepUp'],
                       da['stepDown'],
                       da['biDirectionDwellTime'])
    os.system(cmdStr)
    attnObj = attenuator.Attenuator()
    num_devices = attnObj.find_devices()
    result = attnObj.open_device(1)
    modelName = attnObj.get_modelname(1)
    dllVer = attnObj.get_dllversion()
    serNo = attnObj.get_serial_number(1)
    startAttn = attnObj.get_rampstart(1,1)
    endAttn = attnObj.get_rampend(1,1)
    dwellTime = attnObj.get_dwelltime(1,1)
    idleTime = attnObj.get_idletime(1,1)
    holdTime = attnObj.get_holdtime(1,1)
    bidirDwellTime = attnObj.get_bidirectional_dwelltime(1,1)
    #stepUp = attnObj.get_attenuationstep(1,1)

    print(num_devices)
    print(serNo)
    print(modelName)

    return templates.TemplateResponse('index.html', {'request': request , 'with_attn': dllVer, 'serNo': serNo, 'startAttn': da['startAttn'], 'endAttn': endAttn, 'DwellTime': dwellTime, 'idleTime': idleTime, 'holdTime': holdTime, 'bidirDwellTime': bidirDwellTime})



@app.get('/', response_class=HTMLResponse)
def main(request: Request):
    attnObj = attenuator.Attenuator()
    file_list = ['aptx.csv', 'aac_btc.csv', 'aptx.csv']
    cc = codecomparator.CodecComparator() 
    plt,fig=cc.compareFiles(file_list)
    fig.savefig('my_plot')
    
    
    num_devices = attnObj.find_devices()
    result = attnObj.open_device(1)
    modelName = attnObj.get_modelname(1)
    dllVer = attnObj.get_dllversion()
    serNo = attnObj.get_serial_number(1)
    startAttn = attnObj.get_rampstart(1,1)
    endAttn = attnObj.get_rampend(1,1)
    dwellTime = attnObj.get_dwelltime(1,1)
    idleTime = attnObj.get_idletime(1,1)
    holdTime = attnObj.get_holdtime(1,1)
    bidirDwellTime = attnObj.get_bidirectional_dwelltime(1,1)
    #stepUp = attnObj.get_attenuationstep(1,1)

    print(num_devices)
    print(serNo)
    print(modelName)

    return templates.TemplateResponse('index.html', {'request': request , 'with_attn': dllVer, 'serNo': serNo, 'startAttn': startAttn, 'endAttn': endAttn, 'DwellTime': dwellTime, 'idleTime': idleTime, 'holdTime': holdTime, 'bidirDwellTime': bidirDwellTime})
