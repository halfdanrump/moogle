class CreateFulldocs < ActiveRecord::Migration
  def change
    create_table :fulldocs do |t|
      t.string :code

      t.timestamps
    end
  end
end
