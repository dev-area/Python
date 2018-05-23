#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import abc


class PluginBase(object,metaclass = abc.ABCMeta):
 #   __metaclass__ = abc.ABCMeta 
    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return
    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        return
    
class RegisteredImplementation(object): 
    def load(self, input):
        return input.read()
    def save(self, output, data): 
        return output.write(data)
 
class A(PluginBase):
    def load(self, input):
        return input.read()
    def save(self, output, data): 
        return output.write(data)
    
PluginBase.register(RegisteredImplementation)

