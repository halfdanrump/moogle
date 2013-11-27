class Clinic
  include Mongoid::Document
  field :fulldoc, type: String
  field :h, as :hospital_code, type: String
  field :n, as :name, type: String
  field :p, as :postcode, type: Integer
  field :departments, type: Array #File 2
  field :facilities, type: Array #File 3
  field :machines, type: Array #File 10



  
end
