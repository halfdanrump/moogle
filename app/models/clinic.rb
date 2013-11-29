class Clinic
  include Mongoid::Document
  #include Mongoid::FullTextSearch

  field :fulldoc, type: String
  field :hospital_code, type: String
  field :name, type: String
  field :postcode, type: Integer
  field :departments, type: Array #File 2
  field :facilities, type: Array #File 3
  field :machines, type: Array #File 10


  #fulltext_search_in :fulldoc

  
end
