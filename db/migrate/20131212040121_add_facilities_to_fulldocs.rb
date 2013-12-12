class AddFacilitiesToFulldocs < ActiveRecord::Migration
  def change
    add_column :fulldocs, :facilities, :text
  end
end
