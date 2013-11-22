class Clinic
  include Mongoid::Document
  field :code, type: Integer
  field :name, type: String
  field :postcode, type: Integer
end
