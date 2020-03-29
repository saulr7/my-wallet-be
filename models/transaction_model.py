
class transaction_by_user_model:

    Id              = 0
    Category        = ""
    CategoryId      = 0
    Amount          = 0.00
    CreatedAtDate   = ""
    Comment         = ""


    def __init__(self, Id,Category, CategoryId, Amount, CreatedAtDate, Comment):
        self.Id             = Id
        self.Category       = Category
        self.CategoryId     = CategoryId
        self.Amount         = Amount
        self.CreatedAtDate  = CreatedAtDate
        self.Comment        = Comment
 

    def toDict(self):
        return {
            "Id"            : self.Id,
            "Category"      : self.Category,
            "CategoryId"    : self.CategoryId,
            "Amount"        : float( self.Amount),
            "CreatedAtDate" : str (self.CreatedAtDate),
            "Comment"       : self.Comment,
  
        }
