# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:32:43 2021

@author: Deepa.Mohite
"""

from flask_restful import Resource


class DeploymentTestStream(Resource):
    
    """
    Provide an implementation for the /deploymenttest1/stream'.
    
    @author: Deepa.Mohite    
    """
    
      
    def __init__(self):
        pass
    
    def post(self):
        
        """
        @author: Deepa.Mohite
        """
        
        try :
            
            return "Hello, This is Deployment Test1 Stream Flask App.", 200
       
        except Exception as e:
            print(e)
            return "Hello, This is Deployment Test1 Stream Flask App.", 400