json.array!(@clinics) do |clinic|
  json.extract! clinic, :code, :name, :postcode, :machines
  json.url clinic_url(clinic, format: :json)
end
