package model

type Properties struct {
	quota    int
	property Property
	regNo    string `json:"reg_no"`
}

type Metadata struct {
	id string
}

type Display struct {
	title           string
	subtitle        string
	priceFormattted string `json:"price_formatted"`
	imageURl        string `json:"image_url"`
	typeStr         string `json:"type"`
}

type Property struct {
	metadata Metadata
	display  Display
}
