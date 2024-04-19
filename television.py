class Television():
    
    # Varaibles to declare Min and Max volumes
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    
    # Varaibles to declare the Min and Max channels
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__ (self):
        self.powered = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    #Toggle power state of the TV
    def power(self):
        if(self.powered == True):
            self.powered = False
        elif (self.powered == False):
            self.powered = True
        
    #Toggle Mute state of the TV
    def mute(self):
        if(self.powered == True):
            if(self.muted == True):
                self.muted = False
            elif (self.muted == False):
                self.muted = True

    
    
    #Setters
    def channel_up(self):
        if(self.powered == True):
            if (self.channel == self.MAX_CHANNEL):
                self.channel = self.MIN_CHANNEL
            else:
                self.channel += 1
    
    
    def channel_down(self):
        if(self.powered == True):
            if (self.channel == self.MIN_CHANNEL):
                self.channel = self.MAX_CHANNEL
            else:
                self.channel -= 1

    
    def volume_up(self):
        if(self.powered == True):
            self.muted = False
            
            if (self.volume < self.MAX_VOLUME):
               self.volume +=1
    
    
    def volume_down(self):
        if(self.powered == True):
            self.muted = False
            
            if (self.volume > self.MIN_VOLUME):
                self.volume -= 1
    
    
    
    def __str__(self):
        if (self.muted == True):
            return f"Power = {self.powered}, Channel = {self.channel}, Volume = {0}"
        else:
            return f"Power = {self.powered}, Channel = {self.channel}, Volume = {self.volume}"




