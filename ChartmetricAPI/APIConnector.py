import requests

def connect(refreshtoken):
    #Session
    s = requests.Session()
    #User token
    payload={
        "refreshtoken": refreshtoken,
    }

    #Auth
    try:
        responseAuth=s.post("https://api.chartmetric.com/api/token",data=payload)
        authInfo=responseAuth.json()
        #print(authInfo)
        authToken=authInfo['token']
        if(responseAuth.status_code==200):
            #print("Authorization successfull. Access token: "+authToken)
            return(s,authToken)
        else:
            print("Error: "+responseAuth.status_code)
    except Exception as e:
        print("Authorization went wrong")
        return(e.__str__)