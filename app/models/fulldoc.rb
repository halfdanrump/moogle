class Fulldoc < ActiveRecord::Base
	validates :code, precence: true
	validates :doc, precence: true
end
