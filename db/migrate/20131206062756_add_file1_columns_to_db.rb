class AddFile1ColumnsToDb < ActiveRecord::Migration
  def change
	add_column :fulldocs, :'常勤歯科医師数', :string
	add_column :fulldocs, :'特定機能病院', :string
	add_column :fulldocs, :'開設年月', :string
	add_column :fulldocs, :'特定特別医療法人', :string
	add_column :fulldocs, :'市区郡', :string
	add_column :fulldocs, :'病院日本語名称', :string
	add_column :fulldocs, :'FAX番号', :string
	add_column :fulldocs, :'電話番号', :string
	add_column :fulldocs, :'医療従事者総数', :string
	add_column :fulldocs, :'都道府県', :string
	add_column :fulldocs, :'病院名カナ', :string
	add_column :fulldocs, :'非常勤歯科医師数', :string
	add_column :fulldocs, :'ホームページアドレス', :string
	add_column :fulldocs, :'非常勤医師数', :string
	add_column :fulldocs, :'日本医療機能評価機構認定病院', :string
	add_column :fulldocs, :'経営体', :string
	add_column :fulldocs, :'常勤医師数', :string
	add_column :fulldocs, :'郵便番号', :string
	add_column :fulldocs, :'発行年月日', :string
	add_column :fulldocs, :'住所', :string
	add_column :fulldocs, :'救急告示病院', :string
	add_column :fulldocs, :'地域医療支援', :string
  end
end
