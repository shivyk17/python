# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:23:04 2021

@author: Deepa.Mohite
"""

from flask_restful import Resource


class DeploymentTestUpload(Resource):
    
    """
    Provide an implementation for the /deploymenttest1/upload'.
    
    @author: Deepa.Mohite    
    """  
    
    def __init__(self):
        pass
                
    def post(self):
        """
        @author: Deepa.Mohite
        """
        
        try :
            
            return "Hello, This is Deployment Test1 Upload Flask App.", 200
       
        except Exception as e:
            print(e)
            return "Hello, This is Deployment Test1 Upload Flask App.", 400