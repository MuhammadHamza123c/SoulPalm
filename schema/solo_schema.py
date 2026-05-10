from pydantic import BaseModel, Field
from typing import List, Optional


class PalmOverview(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    aura_type: Optional[str] = None
    energy_level: Optional[int] = Field(default=None, ge=0, le=100)


class PersonalityAnalysis(BaseModel):
    core_personality: Optional[str] = None
    emotional_nature: Optional[str] = None
    intelligence_style: Optional[str] = None
    creativity_level: Optional[int] = Field(default=None, ge=0, le=100)
    leadership_quality: Optional[int] = Field(default=None, ge=0, le=100)
    social_behavior: Optional[str] = None
    hidden_strength: Optional[str] = None
    main_weakness: Optional[str] = None


class EmotionalLoveEnergy(BaseModel):
    love_style: Optional[str] = None
    emotional_depth: Optional[int] = Field(default=None, ge=0, le=100)
    trust_level: Optional[int] = Field(default=None, ge=0, le=100)
    relationship_tendency: Optional[str] = None
    heart_energy: Optional[str] = None


class CareerSuccessPath(BaseModel):
    career_type: Optional[str] = None
    ambition_level: Optional[int] = Field(default=None, ge=0, le=100)
    success_potential: Optional[int] = Field(default=None, ge=0, le=100)
    natural_talents: Optional[List[str]] = None
    future_opportunity: Optional[str] = None


class DestinyFuture(BaseModel):
    life_phase: Optional[str] = None
    future_energy: Optional[str] = None
    personal_transformation: Optional[str] = None
    destiny_direction: Optional[str] = None


class AuraReading(BaseModel):
    aura_color: Optional[str] = None
    spiritual_energy: Optional[str] = None
    inner_power: Optional[str] = None
    energy_description: Optional[str] = None


class LuckyElements(BaseModel):
    lucky_color: Optional[str] = None
    lucky_number: Optional[int] = None
    lucky_day: Optional[str] = None
    spirit_element: Optional[str] = None
    energy_symbol: Optional[str] = None


class DestinyTimeline(BaseModel):
    near_future: Optional[str] = None
    major_turning_point: Optional[str] = None
    long_term_destiny: Optional[str] = None


class OracleMessage(BaseModel):
    quote: Optional[str] = None


class SoloPalmResponse(BaseModel):
    palm_overview: Optional[PalmOverview] = None
    personality_analysis: Optional[PersonalityAnalysis] = None
    emotional_love_energy: Optional[EmotionalLoveEnergy] = None
    career_success_path: Optional[CareerSuccessPath] = None
    destiny_future: Optional[DestinyFuture] = None
    aura_reading: Optional[AuraReading] = None
    lucky_elements: Optional[LuckyElements] = None
    destiny_timeline: Optional[DestinyTimeline] = None
    oracle_message: Optional[OracleMessage] = None