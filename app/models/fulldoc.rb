class Fulldoc < ActiveRecord::Base
	validates :code, presence: true, allow_blank: false
	validates :doc, presence: true, allow_blank: false

	def self.search(terms = "")
	    sanitized = sanitize_sql_array(["to_tsquery('english', ?)", terms.gsub(/\s/,"+")])
	    Fulldoc.where("search_vector @@ #{sanitized}")
  end

  has_one :clinic
end
