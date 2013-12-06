class CreateUniqueColumnHospitalCode < ActiveRecord::Migration
  def change
    remove_column :fulldocs, :code
    add_column :fulldocs, :code, :integer
    add_index :fulldocs, :code, unique: true
  end
end
