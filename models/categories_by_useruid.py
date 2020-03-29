
class categories_by_useruid_model:

    Id = 0
    Category = ""


    def __init__(self, Id,Category):
        self.Id = Id
        self.Category = Category
 

    def toDict(self):
        return {
          "Id" : self.Id,
          "Category" :  self.Category,
  
        }
