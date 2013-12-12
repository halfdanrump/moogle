class ChangeFaxToLowercase < ActiveRecord::Migration
  def up
  	remove_column :fulldocs, :'FAX番号'
  	add_column :fulldocs, :'fax番号', :string
  end
  def down
	remove_column :fulldocs, :'fax番号'
  	add_column :fulldocs, :'FAX番号', :string
  end
end
