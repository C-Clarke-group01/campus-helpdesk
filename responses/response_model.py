from fastapi import status


def SuccessResponseModel(data,message):
    return{
        "status":True,

        "code":status.HTTP_200_OK,
        "message":message
    }

def ErrorResponseModel(error="server error",code=status.HTTP_400_BAD_REQUEST):
    return{
        "status":False,

        "message":error
    }