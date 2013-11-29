class Fulldoc < ActiveRecord::Base
	validates :code, presence: true, allow_blank: false
	validates :doc, presence: true, allow_blank: false
end
