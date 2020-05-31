#
# This the Vector Space Object Definition
#           Date:   1st June 2019
#           Author: Dr. Andrew Blyth, PhD. (andrew.blyth@adisa.global)
# 
# 
# 
# 
# 
import math
#
class VectorSpace():
    #
    # ->    This is the constructor function for the Class/Object-Type: VectorSpace()
    #
    def __init__(self):
        self._DEBUG       = False                  # This is DEBUG switch for the VectorSpace object
        self._radius      = 1000                   # This is the radius at which the prediction partciles ordit.
        self._anglerate   = 0.15                    # This is the rangular rate of turn
        self._safedistane = 150                    # This is the safe distance for a event partcile
        self._plist       = {(0,0,0) : []}         # This is the dictionary of partciles at co-ords x,y,z
                                                   # For example { (X,Y,Z) : (PartcileType, PartcileID) }
    #   
    # ->   This is the vectorSpaceGetParticlePosiution(uT, pT, pID) function for the Class/Object-Type: VectorSpace()
    #       Where: 
    #           pT  -   The Partcile Type
    #           pID -   The Unique ID of the Partcile
    #
    def vectorSpaceGetParticlePosition(self, pT, pID):
        for x, y, z in self._plist: 
            for (pType, pIDent) in self._plist[x,y,z]:
                if (pType == pT and pIDent == pID): return (x, y, z, pID)
    #   
    # ->   This is the vectorSpaceDecayParticle(uT, pT, pID) function for the Class/Object-Type: VectorSpace()
    #       Where: 
    #           pT  -   The Partcile Type
    #           pID -   The Unique ID of the Partcile
    #
    def vectorSpaceDecayParticle(self, pT, pID):
        return True
    #
    # ->   This is the vectorMatrixUpdateEventParticle(uT, pT, pID, eT ,eID) function for the Class/Object-Type: VectorSpace()
    #       Where: 
    #           Ut  -   Utility value for the two particles
    #           pT  -   The Prediction Partcile Type
    #           pID -   The Unique ID of the Prediction Partcile
    #           eT  -   The Event Particle Type
    #           eID -   The Unique ID of the Event Partcile
    #
    def vectorMatrixUpdateEventParticle(self, uT, pT, pID, eT ,eID):
        uT          = float(uT)
        eventX      = 0
        eventX      = 0
        predictionX = 0
        predictionY = 0
        newX        = 0
        newY        = 0
        #
        for x,y,z in self._plist: 
            for (pType,pIDent) in self._plist[x,y,z]:
                if (pType == eT and pIDent == eID ):
                    eventX = x
                    eventY = y
        for x,y,z in self._plist:
            for (pType,pIDent) in self._plist[x,y,z]: 
                if (pType == pT and pIDent == pID ):
                    predictionX = x
                    predictionY = y
        #
        hyp = math.sqrt(((predictionX - eventX) ** 2) + ((predictionY - eventY) ** 2))
        if (hyp > self._safedistane):
            if (predictionX >= eventX and predictionY >= eventY):
                X = predictionX - eventX
                Y = predictionY - eventY
                alpha = math.atan( Y / X )
                newY = (math.sin(alpha) * uT) + eventY
                newX = (math.cos(alpha) * uT) + eventX  
            elif (predictionX >= eventX and predictionY <= eventY):
                X = predictionX - eventX
                Y = predictionY - eventY
                alpha = math.atan( Y / X )
                newY = (math.sin(alpha) * uT) + eventY
                newX = (math.cos(alpha) * uT) + eventX
            elif (predictionX <= eventX and predictionY <= eventY):
                X = predictionX - eventX
                Y = predictionY - eventY
                alpha = math.atan( Y / X ) 
                newY = (0 - math.sin(alpha) * uT) + eventY
                newX = (0 - math.cos(alpha) * uT) + eventX  
            else:
                X = predictionX - eventX
                Y = predictionY - eventY
                alpha = math.atan( Y / X )
                newY = (0 - math.sin(alpha) * uT) + eventY
                newX = (0 - math.cos(alpha) * uT) + eventX   
            #     
            _ = self.updateParticleLocation(newX, newY, 0, eT, eID)     
        #
        return True
    #
    # 
    #  self.updateParticleLocation(newX, newY, newZ, pT, pID)
    # 
    # 
    # 
    #  ->   This is the getParticleList(self, x, y, z) function for the Class/Object-Type: VectorSpace()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               x, y, z     -   This refers to the location of the partcile list.
    #    
    def getParticleList(self, x, y, z):
        try:
            return self._plist[(x, y, z)]
        except:
            return {(x, y, z) : []}
    #
    #  ->   This is the getAllEventParticles(self) function for the Class/Object-Type: VectorSpace()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #    
    def getAllEventParticles(self): 
        returnList = {}
        for x,y,z in self._plist:
            for (pT,pID) in self._plist[x,y,z]:
                if (pT != 'prediction' and pT != 'stix'): 
                    try:
                        returnList[( x, y, z )].append((pT,pID))
                    except:
                        returnList[( x, y, z )] = []
                        returnList[( x, y, z )].append((pT,pID))

        return returnList
    #
    #  ->   This is the getAllSTIXParticles(self) function for the Class/Object-Type: VectorSpace()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #    
    def getAllSTIXParticles(self): 
        returnList = {}
        for x,y,z in self._plist:
            for (pT,pID) in self._plist[x,y,z]:
                if (pT == 'prediction'): 
                    try:
                        returnList[( x, y, z, pID )].append((pT,pID))
                    except:
                        returnList[( x, y, z, pID )] = []
                        returnList[( x, y, z, pID )].append((pT,pID))

        return returnList
    #
    #  ->   This is the addParticleList(self, x, y, z) function for the Class/Object-Type: VectorSpace()
    #       Where: 
    #               self        -   This refers to the object that owns and invokes the function.
    #               x, y, z     -   This refers to the location of the partcile vector space.
    #               particle    -   This refers to the Partcile to be added to the Vector Spave.
    #    
    def addParticleList(self, x, y, z, particle):
        try:
            self._plist[( x, y, z )].append(particle)
        except:
            self._plist[( x, y, z )] = []
            self._plist[( x, y, z )].append(particle)
    #
    #  ->   This is the delParticleList(self, x, y, z) function for the Class/Object-Type: VectorSpace()
    #       Where: 
    #               self                    -   This refers to the object that owns and invokes the function.
    #               particleType, particleID    -   This refers to the Partcile to be deleted to the Vector Spave.
    #    
    def delParticleList(self, particle):
        for x,y,z in self._plist:
            for (pt,pid) in self._plist[x,y,z]:
                if (particle == (pt,pid)):
                    self._plist[x,y,z].remove(particle)
        return True
    #
    #  ->   This is the updateParticleLocation(self, x, y, z) function for the Class/Object-Type: VectorSpace()
    #       Where: 
    #               self                        -   This refers to the object that owns and invokes the function.
    #               x, y, z                     -   This refers to the new location of the partcile vector space.
    #               particleType, particleID    -   This refers to the Partcile to be updates to the Vector Spave.
    #    
    def updateParticleLocation(self, newX, newY, newZ, particleType, particleID):
        particle = (particleType, particleID)
        try:
            if self.delParticleList(particle):
                return self.addParticleList(newX, newY, newZ, (particleType, particleID))
        except:
            return False
    #
    #   ->   This is the distributePredictionParticleinGVSM(self, x, y, z) function for the Class/Object-Type: VectorSpace()
    #       Where: 
    #               self                        -   This refers to the object that owns and invokes the function.
    # 
    def distributePredictionParticleinGVSM(self):
        counter = 0
        for x,y,z in self._plist:
            for (pT,pID) in self._plist[x,y,z]:
                if (pT == 'prediction'): 
                    counter = counter + 1
        #    
        print(counter)    
        degree     = 720 / counter 
        counter    = 0
        updateList = []
        for x,y,z in self._plist:
            for (pT,pID) in self._plist[x,y,z]:
                if (pT == 'prediction'):
                    newX = math.sin(math.radians(counter * degree)) * self._radius
                    newY = math.cos(math.radians(counter * degree)) * self._radius
                    newZ = 0
                    counter = counter + 1
                    if (self._DEBUG):
                        print('******* Prediction Partcile Distribution *******************************************************')
                        print('Partcile ID :', pID)
                        print(' :----> X - Y - Z :', newX ,' - ', newY ,' - ', newZ)
                        sina = newX / self._radius
                        angle = math.degrees(math.asin(sina))
                        ddd = (counter -1)* degree
                        print(' :----> angle - degree  - total:', angle,' - ', ddd,' - ', (angle + ddd))
                        print('')
                    #
                    updateList.append((newX, newY, newZ, pT, pID))
        #
        for (newX, newY, newZ, pT, pID) in updateList: self.updateParticleLocation(newX, newY, newZ, pT, pID)
        #
        return True
    #
    #
    #
    def updatePredictionPartcile(self, particleType, particleID):         
        #
        updateList = []
        for x,y,z in self._plist:
            for (pT,pID) in self._plist[x,y,z]:
                if (pT == particleType):
                    newX = x
                    newY = y
                    newZ = z
                    angle = 0
                    newAngle = 0
                    #
                    if (x >= 0 and y >= 0):
                       sina = x / self._radius
                       angle = math.degrees(math.asin(sina))
                       newAngle = angle + self._anglerate
                       newX = math.sin(math.radians(newAngle)) * self._radius
                       newY = math.cos(math.radians(newAngle)) * self._radius
                    elif (x >= 0 and y <= 0):
                       sina = x / self._radius
                       angle = math.degrees(math.asin(sina))
                       newAngle = angle - self._anglerate
                       newX = math.sin(math.radians(newAngle)) * self._radius
                       newY = 0 - math.cos(math.radians(newAngle)) * self._radius
                    elif (x <= 0 and y <= 0):
                       sina = y / self._radius
                       angle = math.degrees(math.asin(sina))
                       newAngle = angle + self._anglerate
                       newX = 0 - math.cos(math.radians(newAngle)) * self._radius
                       newY = math.sin(math.radians(newAngle)) * self._radius
                    elif (x <= 0 and y >= 0):
                       sina = y / self._radius
                       angle = math.degrees(math.asin(sina))
                       newAngle = angle + self._anglerate
                       newX = 0 - math.cos(math.radians(newAngle)) * self._radius
                       newY = math.sin(math.radians(newAngle)) * self._radius
                    #
                    #
                    if (self._DEBUG):
                        print('-------------------------------------- Prediction Particle Update---------------------------------')
                        print('Partcile ID :', pID)
                        print(' OLD :----> X - Y - Z   :', x ,' - ', y ,' - ', z)
                        print(' NEW :----> X - Y - Z   :', newX ,' - ', newY ,' - ', newZ)
                        print(' ANGLES:--> Old - New   :', angle ,' - ', newAngle)
                    #
                    updateList.append((newX, newY, newZ, pT, pID))
        for (newX, newY, newZ, pT, pID) in updateList: self.updateParticleLocation(newX, newY, newZ, pT, pID)
        return True
#
# -> This is the End of the VectorSpace() Object: Last Edited - Date:   1st June April 2019
#
#