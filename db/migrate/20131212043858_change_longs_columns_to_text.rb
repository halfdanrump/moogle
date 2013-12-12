class ChangeLongsColumnsToText < ActiveRecord::Migration
  def change
  	change_column :fulldocs, :departments, :text
  	change_column :fulldocs, :facilities, :text
  	change_column :fulldocs, :machines, :text
  end
end
