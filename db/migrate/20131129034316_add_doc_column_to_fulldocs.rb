class AddDocColumnToFulldocs < ActiveRecord::Migration
  def change
  	add_column :fulldocs, :doc, :string	
  end
end
