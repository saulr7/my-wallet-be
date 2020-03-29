from datetime import datetime
class category_model:

    Id = 0
    Category = ""
    CategoryTypeId = 0
    Active = False
    CreatedBy = 0
    CreatedAtDate = ""
    CreatedAtTime = ""
    UpdatedAt = ""

    def __init__(self, Id,Category,CategoryTypeId,Active,CreatedBy,CreatedAtDate,CreatedAtTime,UpdatedAt):
        print(UpdatedAt)
        self.Id = Id
        self.Category = Category
        self.CategoryTypeId = CategoryTypeId
        self.Active = Active
        self.CreatedBy = CreatedBy
        self.CreatedAtDate = CreatedAtDate
        self.CreatedAtTime = CreatedAtTime
        self.UpdatedAt =  UpdatedAt

    def toDict(self):
        return {
          "Id" : self.Id,
          "Category" :  self.Category,
          "CategoryTypeId" :  self.CategoryTypeId,
          "Active" :  self.Active,
          "CreatedBy" :  self.CreatedBy,
          "CreatedAtDate" :  str( self.CreatedAtDate),
          "CreatedAtTime" :  str( self.CreatedAtTime),
          "UpdatedAt" :     str(  self.UpdatedAt) 
        }
