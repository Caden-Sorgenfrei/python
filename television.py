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
        self.volume = 0
        self.channel = 0

    def power(self):
        if(self.powered == True):
            self.powered = False
        elif (self.powered == False):
            self.powered = True
        
    
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
    
    
    
    #Getters
    def get_power(self):
        return self.powered
    
    def get_volume(self):
        if(self.muted == True):
            return 0
        return self.volume
    
    def get_channel(self):
        return self.channel
    
    
    
    def __str__(self):
        
        return f"Power = {self.get_power()}, Channel = {self.get_channel()}, Volume = {self.get_volume()}, Muted: {self.muted}"

