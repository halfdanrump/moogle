class ChangeTypeOfFulldocToText < ActiveRecord::Migration
  def change
  	remove_column :fulldocs, :doc
  	add_column :fulldocs, :doc, :text
  end
end
