
__all__ = ["TriggerInfo"]


from Gaugi.messenger import Logger
from Gaugi.messenger.macros import *


#
# Trigger info
#
class TriggerInfo(Logger):
  
  #
  # Constructor
  #
  def __init__(self, chain):

    Logger.__init__(self)
    # Compile all internal variables
    self.compile(trigger)


  #
  # Compile the trigger flags from the chain name
  #
  def compile(self, trigger):

    self.__trigger = trigger

    if trigger.startswith('HLT_'):
      trigger = trigger.replace( 'HLT_','')
      
    trigParts = trigger.split('_')

    part = trigParts[0]
    if part[0]=='e':
      self.__signature = 'electron'
    elif part[0]=='g':
      self.__signature = 'photon'
    else:
      self.__signature = None

    self.__etthr = float( part[1::] )

    # Get the operation point
    pidword = 'lhvloose'
    if 'lhtight' in trigParts[-1]:
      pidword = 'lhtight'
    elif 'lhmedium' in trigParts[-1]:
      pidword = 'lhmedium'
    elif 'lhloose' in trigParts[-1]:
      pidword = 'lhloose'
    elif 'lhvloose' in trigParts[-1]:
      pidword = 'lhvloose'
    else: 
      MSG_WARNING( self, "No Pid name was fount in the expression (%s) with path (%s)", self.expression(), trigParts[-1])
 
    self.__pidname = pidword
    # check the ringer flag
    if 'noringer' in trigger:
      self.__ringer = False
    elif 'ringer' in trigger:
      self.__ringer = True
    else:
      self.__ringer = True

  
  #
  # Get the signature
  #
  def signature(self):
    return self.__signature

  #
  # Get the eT threshold
  #
  def etthr(self):
    return self.__etthr

  #
  # Is a ringer chain?
  #
  def ringer(self):
    return self.__ringer

  #
  # Get the chain name
  #
  def trigger(self):
    return self.__trigger

  #
  # Get the  operation point
  #
  def pidname(self):
    return self.__pidname



