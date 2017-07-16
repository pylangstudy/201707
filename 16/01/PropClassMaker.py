class PropClassMaker:
    @staticmethod
    def Create(class_name:str, properties):
        cls_type = type(class_name, (object,), {})  
#        cls_type['__slots__'] = properties # TypeError: 'type' object does not support item assignment
#        cls_type.__dict__['__slots__'] = properties # TypeError: 'mappingproxy' object does not support item assignment    
        return cls_type
#    def __create_property(self, cls_type, prop_name):
#        cls_type.__dict__[prop_name] = property(lambda x: , setx, delx, "I'm the 'x' property.")


cls = PropClassMaker.Create('Human', ['name', 'age'])
print(cls)
print(dir(cls()))

#import types
#print(dir(types.GetSetDescriptorType))
