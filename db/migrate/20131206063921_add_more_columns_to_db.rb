class AddMoreColumnsToDb < ActiveRecord::Migration
  def change
  	add_column :fulldocs, :departments, :string
  	add_column :fulldocs, :machines, :string
  end
end
