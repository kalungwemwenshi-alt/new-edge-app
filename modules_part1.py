# modules_part1.py
# Comprehensive content for Module 1 & Module 2

MODULE_1 = """            <!-- MODULE 1 -->
            <div class="module-content-pane active" id="module-1">
                <div class="module-hero">
                    <span class="module-number">The Institutional Foundation</span>
                    <h1>Module 1: Foundation of an Institutional Trader</h1>
                    <p>Deconstructing the $7.5 Trillion marketplace architecture, the central limit order book (CLOB), algorithmic price delivery (IPDA), and the AMD execution cycle.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: 12.5%;"></div>
                    </div>
                </div>

                <!-- 1. THE ARCHITECTURE OF FOREX -->
                <div class="content-section">
                    <h3><i class='bx bx-globe'></i> 1. The True Architecture of Forex & The $7.5T CLOB</h3>
                    <p>Foreign Exchange is not an open, egalitarian casino. It is a decentralized, over-the-counter (OTC) institutional liquidity network processing over <strong>$7.5 trillion daily</strong>. Retail traders account for less than 5.5% of total volume. The remaining 94.5% is dominated by sovereign wealth funds, multinational corporations, central banks, and Tier-1 market-making investment banks (JPMorgan, Deutsche Bank, Citi, UBS).</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid var(--vip-gold);">
                            <h4 style="color: var(--vip-gold); margin-bottom: 8px;">The Interbank Wholesale Layer (Tier-1 ECNs)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Aggregated through primary matching engines like EBS (Electronic Broking Services) and Refinitiv (Reuters Dealing 3000). Prices fluctuate in sub-pip fractions with deep limit liquidity books. Spreads are near 0.0 pips.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #ff4444;">
                            <h4 style="color: #ff4444; margin-bottom: 8px;">The Retail "B-Book" Illusion</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Over 80% of retail brokers operate a "B-Book" warehouse model. They do not route your order to the interbank market; they take the other side of your trade. When you lose, the broker profits. They design platforms with artificial slippage, spread markups, and stop-hunt spikes.</p>
                        </div>
                    </div>

                    <div class="key-takeaways" style="margin-top: 25px;">
                        <h4>The Institutional Order Hierarchy</h4>
                        <ul>
                            <li><strong>Tier-1 Prime Brokers & Market Makers:</strong> Control order routing and quote the bid/ask spread to secondary market participants.</li>
                            <li><strong>Central Banks:</strong> Non-commercial participants who execute monetary policy regardless of technical chart patterns.</li>
                            <li><strong>Macro Hedge Funds & Institutional Desks:</strong> Directional participants who must accumulate massive positions over days/weeks without moving market average prices against themselves.</li>
                            <li><strong>Retail Traders:</strong> The ultimate source of resting liquidity (stop losses) exploited by algorithmic execution models.</li>
                        </ul>
                    </div>

                    <!-- SVG 1: Market Hierarchy Schematic -->
                    <div class="illustration-container">
                        <div style="background: #080808; border: 1px solid #222; border-radius: 16px; padding: 20px; overflow-x: auto;">
                            <svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg" style="width: 100%; min-width: 680px; height: auto; display: block;">
                                <line x1="100" y1="20" x2="700" y2="20" stroke="#1a1a1a" stroke-dasharray="4,4" />
                                <line x1="100" y1="90" x2="700" y2="90" stroke="#1a1a1a" stroke-dasharray="4,4" />
                                <line x1="100" y1="165" x2="700" y2="165" stroke="#1a1a1a" stroke-dasharray="4,4" />
                                <line x1="100" y1="240" x2="700" y2="240" stroke="#1a1a1a" stroke-dasharray="4,4" />

                                <polygon points="400,30 490,90 310,90" fill="rgba(214, 255, 0, 0.15)" stroke="var(--vip-gold)" stroke-width="2" />
                                <text x="400" y="65" fill="var(--vip-gold)" font-size="13" font-weight="800" text-anchor="middle">TIER-1 LIQUIDITY POOL</text>
                                <text x="400" y="80" fill="#bbb" font-size="9" text-anchor="middle">JPMorgan, Deutsche Bank, UBS (Interbank Core)</text>

                                <polygon points="310,95 490,95 560,165 240,165" fill="rgba(0, 255, 136, 0.1)" stroke="#00ff88" stroke-width="1.5" />
                                <text x="400" y="130" fill="#00ff88" font-size="13" font-weight="700" text-anchor="middle">CENTRAL BANKS & SOVEREIGN FUNDS</text>
                                <text x="400" y="148" fill="#aaa" font-size="9" text-anchor="middle">FED, ECB, BOJ, SNB (Policy & Currency Pegs)</text>

                                <polygon points="240,170 560,170 630,240 170,240" fill="rgba(0, 191, 255, 0.08)" stroke="#00bfff" stroke-width="1.5" />
                                <text x="400" y="205" fill="#00bfff" font-size="13" font-weight="700" text-anchor="middle">INSTITUTIONAL SPECULATORS & PROPS</text>
                                <text x="400" y="222" fill="#aaa" font-size="9" text-anchor="middle">Macro Hedge Funds, Real Money Desks, CTAs</text>

                                <rect x="120" y="248" width="560" height="52" fill="rgba(255, 68, 68, 0.12)" stroke="#ff4444" stroke-width="1.5" stroke-dasharray="4,4" rx="6" />
                                <text x="400" y="275" fill="#ff4444" font-size="13" font-weight="800" text-anchor="middle">RETAIL HERD (THE FUEL / LIQUIDITY POOL)</text>
                                <text x="400" y="292" fill="#ff8888" font-size="10" text-anchor="middle">Stop Losses & Breakout Chasers Harvested by Algos</text>

                                <path d="M 80 270 L 80 50" stroke="var(--vip-gold)" stroke-width="2" marker-end="url(#m1ArrowUpGold)" fill="none" />
                                <text x="65" y="160" fill="var(--vip-gold)" font-size="10" font-weight="700" text-anchor="middle" transform="rotate(-90 65 160)">CAPITAL EXTRACTION FLOW</text>

                                <path d="M 720 50 L 720 270" stroke="#00ff88" stroke-width="2" marker-end="url(#m1ArrowDownGreen)" fill="none" />
                                <text x="735" y="160" fill="#00ff88" font-size="10" font-weight="700" text-anchor="middle" transform="rotate(90 735 160)">ALGORITHMIC EXECUTION</text>

                                <defs>
                                    <marker id="m1ArrowUpGold" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
                                        <path d="M 4 0 L 8 8 L 0 8 Z" fill="var(--vip-gold)" />
                                    </marker>
                                    <marker id="m1ArrowDownGreen" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
                                        <path d="M 4 8 L 8 0 L 0 0 Z" fill="#00ff88" />
                                    </marker>
                                </defs>
                            </svg>
                        </div>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">The Interbank Hierarchy: Capital flows upward from uncoordinated retail participants to algorithmic market operators.</p>
                    </div>
                </div>

                <!-- 2. IPDA: ALGORITHMIC PRICE DELIVERY -->
                <div class="content-section">
                    <h3><i class='bx bx-chip'></i> 2. The Algorithmic Delivery Engine (IPDA)</h3>
                    <p>Price in modern forex is not determined by an open outcry pit of yelling human traders. It is governed by closed institutional proprietary algorithms known as the <strong>Interbank Price Delivery Engine (IPDA)</strong>. IPDA operates on discrete logic routines designed to achieve two perpetual objectives:</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">Objective A: Rebalance Inefficiencies (Fair Value)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">When aggressive institutional volume moves price rapidly, it leaves behind price voids (Fair Value Gaps). IPDA systematically returns to these price ranges to offer two-sided trading and balance the books.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid var(--vip-gold);">
                            <h4 style="color: var(--vip-gold); margin-bottom: 8px;">Objective B: Neutralize Resting Liquidity (Stop Sweeps)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">IPDA knows precisely where retail stop-loss clusters and breakout buy/sell stop orders reside: above equal highs and below equal lows. Price is dynamically steered into these pools to clear the book.</p>
                        </div>
                    </div>

                    <div class="key-takeaways" style="margin-top: 25px;">
                        <h4>The 3 IPDA Lookback Data Windows</h4>
                        <ul>
                            <li><strong>20-Day Lookback Window:</strong> The institutional monthly liquidity cycle. Highs and lows of the last 20 trading days are prime targets for liquidity sweeps.</li>
                            <li><strong>40-Day Lookback Window:</strong> The quarterly intermediate cycle. Used by commercial operators to rebalance swing portfolios.</li>
                            <li><strong>60-Day Lookback Window:</strong> The major macro trend cycle. Defines key institutional premium and discount boundaries.</li>
                        </ul>
                    </div>
                </div>

                <!-- 3. THE AMD CYCLE -->
                <div class="content-section">
                    <h3><i class='bx bx-refresh'></i> 3. The Institutional AMD Cycle (Power of 3)</h3>
                    <p>Every single institutional move across all liquid timeframes (from the Daily candle down to the 1-Minute chart) follows a recurring 3-stage mechanical cycle: <strong>Accumulation, Manipulation, and Distribution (AMD)</strong>, also termed Wyckoff's <em>Spring/Upthrust</em> or ICT's <em>Power of 3 (PO3)</em>.</p>

                    <div class="illustration-container">
                        <div style="background: #080808; border: 1px solid #222; border-radius: 16px; padding: 20px; overflow-x: auto;">
                            <svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg" style="width: 100%; min-width: 680px; height: auto; display: block;">
                                <rect x="40" y="110" width="220" height="80" fill="rgba(214, 255, 0, 0.05)" stroke="var(--vip-gold)" stroke-width="1" stroke-dasharray="3,3" rx="4" />
                                <text x="150" y="98" fill="var(--vip-gold)" font-size="12" font-weight="700" text-anchor="middle">1. ACCUMULATION (ASIAN CHOP)</text>

                                <rect x="250" y="195" width="160" height="95" fill="rgba(255, 68, 68, 0.08)" stroke="#ff4444" stroke-width="1" stroke-dasharray="3,3" rx="4" />
                                <text x="330" y="305" fill="#ff4444" font-size="12" font-weight="700" text-anchor="middle">2. MANIPULATION (JUDAS SWING)</text>

                                <rect x="410" y="40" width="350" height="240" fill="rgba(0, 255, 136, 0.05)" stroke="#00ff88" stroke-width="1" stroke-dasharray="3,3" rx="4" />
                                <text x="585" y="30" fill="#00ff88" font-size="12" font-weight="700" text-anchor="middle">3. DISTRIBUTION (LONDON / NY TREND)</text>

                                <path d="M 50 150 Q 80 120 110 160 T 170 140 T 230 160 L 290 155 L 330 265 L 360 210 L 440 180 L 510 110 L 590 125 L 680 60 L 740 70" 
                                      fill="none" stroke="#FFFFFF" stroke-width="2.5" />

                                <line x1="50" y1="125" x2="270" y2="125" stroke="#aaa" stroke-width="1" stroke-dasharray="2,2" />
                                <text x="280" y="122" fill="#aaa" font-size="9">Asian High (BSL)</text>
                                <line x1="50" y1="175" x2="290" y2="175" stroke="#aaa" stroke-width="1" stroke-dasharray="2,2" />
                                <text x="300" y="172" fill="#aaa" font-size="9">Asian Low (SSL)</text>

                                <circle cx="330" cy="265" r="14" fill="rgba(255, 68, 68, 0.3)" stroke="#ff4444" stroke-width="2" />
                                <text x="330" y="250" fill="#ff4444" font-size="10" font-weight="800" text-anchor="middle">SWEEP SSL</text>

                                <line x1="360" y1="155" x2="480" y2="155" stroke="var(--vip-gold)" stroke-width="1.5" stroke-dasharray="3,3" />
                                <text x="420" y="150" fill="var(--vip-gold)" font-size="10" font-weight="700">CHoCH / BOS</text>

                                <rect x="420" y="165" width="40" height="35" fill="rgba(214, 255, 0, 0.2)" stroke="var(--vip-gold)" stroke-width="1" />
                                <text x="440" y="215" fill="var(--vip-gold)" font-size="9" text-anchor="middle">RETEST POI</text>

                                <line x1="410" y1="60" x2="740" y2="60" stroke="#00ff88" stroke-width="1" stroke-dasharray="3,3" />
                                <text x="745" y="64" fill="#00ff88" font-size="10" font-weight="700">TARGET: HTF BSL</text>
                            </svg>
                        </div>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">The AMD Model: Range bound accumulation during Asia, violent fake manipulation (Judas Swing) at London open to collect retail sell stops, followed by true directional distribution.</p>
                    </div>

                    <div class="grid-2" style="margin-top: 20px;">
                        <div class="sd-step-card">
                            <div class="sd-step-num">A</div>
                            <strong style="color: var(--vip-gold); font-size: 14px;">1. Accumulation Phase</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Smart money quietly matches buy and sell limits inside an equilibrium consolidation without moving price. Retail traders mark the highs and lows as rigid support/resistance lines.</p>
                        </div>
                        <div class="sd-step-card">
                            <div class="sd-step-num">M</div>
                            <strong style="color: #ff4444; font-size: 14px;">2. Manipulation (Judas Swing)</strong>
                            <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">A rapid algorithmic thrust in the opposite direction of the true day's intention. It traps breakout traders and triggers stop losses, creating the liquidity banks need to fill their massive position.</p>
                        </div>
                    </div>
                </div>

                <!-- 4. COMPARISON TABLE -->
                <div class="content-section">
                    <h3><i class='bx bx-table'></i> 4. Market Participant Structural Matrix</h3>
                    <p>Understanding where each participant operates, their order book mechanics, and how smart money leverages retail vulnerabilities.</p>

                    <div class="sd-table-container">
                        <table class="sd-table">
                            <thead>
                                <tr>
                                    <th>Participant</th>
                                    <th>Order Type</th>
                                    <th>Holding Horizon</th>
                                    <th>Vulnerability</th>
                                    <th>Smart Money Exploit</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Tier-1 Investment Banks</strong></td>
                                    <td>Passive Limit Ladders (CLOB)</td>
                                    <td>Intraday to Multi-Day</td>
                                    <td>Massive size causing slippage</td>
                                    <td>Engineers fake breakouts to source liquidity</td>
                                </tr>
                                <tr>
                                    <td><strong>Central Banks (FED / ECB)</strong></td>
                                    <td>Macro Policy Mandates</td>
                                    <td>Quarterly to Multi-Year</td>
                                    <td>Macroeconomic shocks</td>
                                    <td>Controls interest rate differentials & swap rates</td>
                                </tr>
                                <tr>
                                    <td><strong>Macro Hedge Funds</strong></td>
                                    <td>Large Sized Market & Algorithmic</td>
                                    <td>Weeks to Months</td>
                                    <td>Fixed Stop Boundaries</td>
                                    <td>Hunted at HTF key levels prior to major trends</td>
                                </tr>
                                <tr>
                                    <td><strong>Retail Herd (B-Book)</strong></td>
                                    <td>Aggressive Market Orders (FOMO)</td>
                                    <td>Minutes to Hours</td>
                                    <td>Tight stops behind textbook S/R</td>
                                    <td>Harvested as primary liquidity fuel</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 5. INTERACTIVE TOOL -->
                <div class="content-section">
                    <h3><i class='bx bx-calculator'></i> 5. VIP Interactive Tool: Institutional Order Flow & Absorption Simulator</h3>
                    <p>Simulate how an institutional block order interacts with order book depth vs retail market orders, demonstrating why retail breakouts experience severe slippage and reversal traps.</p>

                    <div class="tool-card" style="margin-top: 20px;">
                        <div class="tool-header">
                            <h4><i class='bx bx-analyse'></i> Institutional Order Flow Terminal</h4>
                            <span class="badge-institutional">MODULE 1 ENGINE</span>
                        </div>

                        <div class="grid-2">
                            <div class="form-group">
                                <label><i class='bx bx-coin'></i> Institutional Order Size (Lots)</label>
                                <select id="m1OrderSize">
                                    <option value="500">500 Lots ($50M Notional) - Medium Desk</option>
                                    <option value="2000">2,000 Lots ($200M Notional) - Heavy Macro Desk</option>
                                    <option value="5000">5,000 Lots ($500M Notional) - Sovereign / Tier-1</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-water'></i> Available Resting Liquidity at Level</label>
                                <select id="m1RestingLiquidity">
                                    <option value="low">Low Liquidity (Retail Range / Mid-Chop)</option>
                                    <option value="medium">Medium Liquidity (Obvious Trendline)</option>
                                    <option value="high">High Liquidity (Equal Highs / Asian Low Sweep)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-transfer'></i> Execution Method</label>
                                <select id="m1ExecutionType">
                                    <option value="market">Aggressive Market Sweep (Consumes Book)</option>
                                    <option value="passive">Passive Limit Absorption + Judas Spike</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-shield'></i> Retail Positioning Status</label>
                                <select id="m1RetailState">
                                    <option value="trapped">80%+ Heavily Trapped Long/Short</option>
                                    <option value="balanced">50/50 Indecisive Distribution</option>
                                </select>
                            </div>
                        </div>

                        <button class="calc-btn" onclick="simulateOrderFlow()" style="margin-top: 15px;">
                            <i class='bx bx-play-circle'></i> Run Order Flow Simulation
                        </button>

                        <div id="m1ResultContainer" class="calc-result" style="display: none; text-align: left; margin-top: 25px; padding: 25px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 12px; margin-bottom: 15px;">
                                <div class="label" style="font-size: 13px; font-weight: 700; color: #fff;">EXECUTION FOOTPRINT AUDIT</div>
                                <div id="m1GradeBadge" class="badge-aaa">OPTIMAL INSTITUTIONAL FILL</div>
                            </div>
                            <div class="value" id="m1SlippageValue" style="text-align: center; font-size: 36px; margin: 15px 0;">0.2 Pips Slippage</div>
                            <p id="m1Summary" style="font-size: 13px; line-height: 1.6; color: #ccc; margin-bottom: 15px;"></p>
                            <div id="m1Directive" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; border-left: 3px solid var(--vip-gold); font-size: 13px; line-height: 1.6; color: #fff;"></div>
                        </div>
                    </div>
                </div>

                <!-- 6. VIP CHECKLIST -->
                <div class="content-section">
                    <h3><i class='bx bx-check-double'></i> 6. The VIP Institutional Foundation Checklist</h3>
                    <p>Internalize these 7 foundational laws before looking at a candlestick chart:</p>

                    <div class="sd-step-card">
                        <div class="sd-step-num">1</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Acknowledge the Counterparty:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never view price as a moving average cross. Always ask: <em>"Whose stop loss is paying for this move?"</em></p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">2</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">B-Book Defense:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never trade with unregulated offshore bucket shops. Use reputable, raw-spread ECN brokers with verified liquidity connections.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">3</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Map Asian Range First:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Always box the Asian session high and low. Expect the London session to engineer a false breakout (Judas Swing) before distributing.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">4</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Treat Losses as Wholesale Cost:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">An institutional operator treats a stopped-out trade as an unavoidable inventory expense, not an attack on personal ego.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">5</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Never Chase Breakouts:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Breakouts into clear support/resistance lines are 85% likely to be liquidity collection runs engineered by algorithmic market makers.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">6</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Strict 20-Day Cycle Context:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Identify whether current price is near the 20-day high (Premium) or 20-day low (Discount) before formulating directional bias.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">7</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Trade the Footprint, Not the Opinion:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never argue with market structure. Trade purely what the institutional order flow displays, regardless of personal macro bias.</p>
                    </div>
                </div>

                <!-- 7. VIDEO MASTERCLASS -->
                <div class="yt-player-section">
                    <h3><i class='bx bxl-youtube' style="color:#FF0000"></i> Module 1 Masterclass: Institutional Forex Architecture</h3>
                    <div class="yt-embed-wrapper">
                        <iframe src="https://www.youtube.com/embed/sQBTswIavnw?rel=0&modestbranding=1"
                            title="Institutional Forex Architecture"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>
                    <div class="key-takeaways" style="margin-top: 20px;">
                        <h4>Masterclass Key Timestamps & Topics</h4>
                        <ul>
                            <li><strong>00:00 - 15:30:</strong> The $7.5 Trillion Marketplace & Central Limit Order Book reality.</li>
                            <li><strong>15:31 - 32:45:</strong> The Interbank Price Delivery Algorithm (IPDA) & 20/40/60 Lookback Cycles.</li>
                            <li><strong>32:46 - 54:10:</strong> Deconstructing the AMD (Accumulation, Manipulation, Distribution) Power of 3 Setup.</li>
                        </ul>
                    </div>
                </div>

                <!-- NAVIGATION -->
                <div class="content-nav">
                    <button class="nav-btn" disabled><i class='bx bx-left-arrow-alt'></i> Previous</button>
                    <button class="nav-btn primary" onclick="showModule(2)">Next: Market Structure <i class='bx bx-right-arrow-alt'></i></button>
                </div>
            </div>
"""

MODULE_2 = """            <!-- MODULE 2 -->
            <div class="module-content-pane" id="module-2">
                <div class="module-hero">
                    <span class="module-number">Technical Control</span>
                    <h1>Module 2: Market Structure & Institutional Bias Mastery</h1>
                    <p>Mastering directional control, BOS vs CHoCH validation, strong vs weak swing points, multi-timeframe structural mapping, and the institutional equilibrium.</p>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill" style="width: 25%;"></div>
                    </div>
                </div>

                <!-- 1. THE INSTITUTIONAL LENS OF STRUCTURE -->
                <div class="content-section">
                    <h3><i class='bx bx-line-chart'></i> 1. The Institutional Lens of Market Structure</h3>
                    <p>Retail textbooks teach traders that market structure is simply "higher highs and higher lows." In reality, institutions view market structure as an algorithmic map of <strong>protected capital allocations</strong>. Swing points are not arbitrary pivots; they are the price levels where banks have resting defense orders to protect their accumulated inventory.</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">Strong / Protected Highs & Lows</h4>
                            <p style="font-size: 13px; line-height: 1.6;">A swing low is only deemed <strong>Strong (Protected)</strong> if it successfully created displacement that broke an opposing swing high (BOS). Institutions have capital defended at this low. It is protected with limit orders.</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #ff4444;">
                            <h4 style="color: #ff4444; margin-bottom: 8px;">Weak / Target Highs & Lows</h4>
                            <p style="font-size: 13px; line-height: 1.6;">A swing low that fails to break structure to the upside is mathematically <strong>Weak</strong>. It offers zero institutional support and serves as an algorithmic liquidity target pool that will be hunted.</p>
                        </div>
                    </div>

                    <div class="key-takeaways" style="margin-top: 25px;">
                        <h4>The 3 Rules of Structural Validity</h4>
                        <ul>
                            <li><strong>Candle Body Close Rule:</strong> A Break of Structure (BOS) requires a complete candle body close beyond the prior swing high/low on the execution timeframe. A wick-only breach is a Liquidity Sweep (SFP), not a structural break.</li>
                            <li><strong>Displacement Requirement:</strong> Valid structural breaks must be accompanied by explosive ERCs (Extended Range Candles) leaving behind imbalances (FVGs). Small-bodied candles indicate retail consolidation.</li>
                            <li><strong>Origin of the Move:</strong> The swing high/low that caused the structural displacement is marked as your institutional Point of Interest (POI).</li>
                        </ul>
                    </div>
                </div>

                <!-- 2. BOS VS CHOCH: SCHEMATIC -->
                <div class="content-section">
                    <h3><i class='bx bx-git-repo-forked'></i> 2. BOS vs CHoCH: The Candlestick Anatomy</h3>
                    <p>Understanding the difference between a trend continuation <strong>BOS (Break of Structure)</strong> and an institutional trend reversal <strong>CHoCH (Change of Character)</strong> is what separates profitable operators from retail breakout victims.</p>

                    <!-- SVG 2: BOS vs CHoCH Schematic -->
                    <div class="illustration-container">
                        <div style="background: #080808; border: 1px solid #222; border-radius: 16px; padding: 20px; overflow-x: auto;">
                            <svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg" style="width: 100%; min-width: 680px; height: auto; display: block;">
                                <!-- Bearish Sequence to Bullish CHoCH -->
                                <polyline points="50,60 140,190 200,130 290,250 350,190 420,290" fill="none" stroke="#ff4444" stroke-width="2.5" />
                                
                                <!-- Labels Strong Highs -->
                                <circle cx="50" cy="60" r="5" fill="#00ff88" />
                                <text x="50" y="45" fill="#00ff88" font-size="10" font-weight="700" text-anchor="middle">Strong High</text>

                                <circle cx="200" cy="130" r="5" fill="#00ff88" />
                                <text x="200" y="115" fill="#00ff88" font-size="10" font-weight="700" text-anchor="middle">Strong High</text>

                                <circle cx="350" cy="190" r="5" fill="#00ff88" />
                                <text x="350" y="175" fill="#00ff88" font-size="10" font-weight="700" text-anchor="middle">Last Strong High</text>

                                <!-- BOS Lines -->
                                <line x1="140" y1="190" x2="300" y2="190" stroke="#555" stroke-dasharray="3,3" />
                                <text x="230" y="185" fill="#888" font-size="9">BOS (Continuation)</text>

                                <line x1="290" y1="250" x2="430" y2="250" stroke="#555" stroke-dasharray="3,3" />
                                <text x="360" y="245" fill="#888" font-size="9">BOS (Continuation)</text>

                                <!-- Reversal Arc -->
                                <path d="M 420 290 L 480 290 L 540 140 L 590 195 L 680 90 L 750 110" fill="none" stroke="#00ff88" stroke-width="3" />
                                <circle cx="420" cy="290" r="6" fill="#ff4444" />
                                <text x="420" y="310" fill="#ff4444" font-size="10" font-weight="800" text-anchor="middle">SWEEP OF SSL</text>

                                <!-- CHoCH Line -->
                                <line x1="350" y1="190" x2="560" y2="190" stroke="var(--vip-gold)" stroke-width="2" stroke-dasharray="4,4" />
                                <text x="480" y="180" fill="var(--vip-gold)" font-size="12" font-weight="800">BULLISH CHoCH</text>
                                <text x="480" y="205" fill="#aaa" font-size="8">Full Candle Body Close Above Last High</text>

                                <!-- Mitigation & Entry -->
                                <rect x="570" y="180" width="40" height="30" fill="rgba(0, 255, 136, 0.15)" stroke="#00ff88" stroke-width="1.5" />
                                <text x="590" y="225" fill="#00ff88" font-size="9" font-weight="700" text-anchor="middle">DEMAND POI RETEST</text>

                                <!-- New BOS Bullish -->
                                <line x1="540" y1="140" x2="700" y2="140" stroke="#00ff88" stroke-dasharray="3,3" />
                                <text x="630" y="135" fill="#00ff88" font-size="9">BOS (Bullish Flow)</text>
                            </svg>
                        </div>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">Structural Reversal Anatomy: Downtrend prints consecutive Strong Highs and BOS. A liquidity sweep at the extreme is followed by displacement breaking the last Strong High (CHoCH), opening the door for discount retest execution.</p>
                    </div>
                </div>

                <!-- 3. PREMIUM VS DISCOUNT ARRAYS -->
                <div class="content-section">
                    <h3><i class='bx bx-slider-alt'></i> 3. Premium vs Discount Arrays & The 50% Rule</h3>
                    <p>Institutions are commercial enterprises. They refuse to buy at wholesale highs or sell at bargain lows. Every dealing range is bisected into <strong>Premium (above 50% equilibrium)</strong> and <strong>Discount (below 50% equilibrium)</strong>.</p>

                    <div class="grid-2">
                        <div class="example-box" style="border-left: 4px solid #ff4444;">
                            <h4 style="color: #ff4444; margin-bottom: 8px;">The Premium Zone (> 50% to 100%)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Where price is considered expensive. Institutions look strictly to offload long inventory and execute <strong>Short Setups</strong> inside Premium arrays (Supply Zones, Bearish Order Blocks, Bearish FVGs).</p>
                        </div>
                        <div class="example-box" style="border-left: 4px solid #00ff88;">
                            <h4 style="color: #00ff88; margin-bottom: 8px;">The Discount Zone (< 50% to 0%)</h4>
                            <p style="font-size: 13px; line-height: 1.6;">Where price is considered cheap. Institutions look strictly to accumulate size and execute <strong>Long Setups</strong> inside Discount arrays (Demand Zones, Bullish Order Blocks, Bullish FVGs).</p>
                        </div>
                    </div>

                    <div class="key-takeaways" style="margin-top: 25px;">
                        <h4>The Optimal Trade Entry (OTE) Golden Ratio</h4>
                        <p style="font-size: 13px; color: #ccc;">When measuring an institutional impulse leg with Fibonacci retracement from swing low to swing high, the highest mathematical probability for sniper reversal lies inside the <strong>62% to 79% retracement band (OTE)</strong>. Entering at the 50% equilibrium carries acceptable probability, but 62%-79% yields institutional 1:5+ R:R efficiency.</p>
                    </div>
                </div>

                <!-- 4. COMPARISON TABLE -->
                <div class="content-section">
                    <h3><i class='bx bx-table'></i> 4. Structural Break Classification Table</h3>
                    <p>Classify every structural event with mechanical rigor to eliminate subjective emotional bias.</p>

                    <div class="sd-table-container">
                        <table class="sd-table">
                            <thead>
                                <tr>
                                    <th>Event</th>
                                    <th>Candle Requirement</th>
                                    <th>Institutional Meaning</th>
                                    <th>Actionable Bias</th>
                                    <th>Execution Grade</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>BOS (Break of Structure)</strong></td>
                                    <td>Full body close past swing extreme</td>
                                    <td>Institutional trend continuation</td>
                                    <td>Trade pullbacks in trend direction</td>
                                    <td><span class="badge-aaa">GRADE AAA</span></td>
                                </tr>
                                <tr>
                                    <td><strong>CHoCH (Change of Character)</strong></td>
                                    <td>Full body close breaking origin high/low</td>
                                    <td>Order flow transition & trend shift</td>
                                    <td>Wait for discount/premium POI retest</td>
                                    <td><span class="badge-aaa">GRADE AAA</span></td>
                                </tr>
                                <tr>
                                    <td><strong>Liquidity Sweep / SFP</strong></td>
                                    <td>Wick breaches high/low; body closes inside</td>
                                    <td>Stop hunt / liquidity harvesting</td>
                                    <td>Fade the fake breakout instantly</td>
                                    <td><span class="badge-b">GRADE B (SNIPER)</span></td>
                                </tr>
                                <tr>
                                    <td><strong>Minor Sub-Structure Break</strong></td>
                                    <td>Internal candles inside parent leg</td>
                                    <td>Corrective pullback noise</td>
                                    <td>Do NOT trade against parent leg</td>
                                    <td><span class="badge-c">AVOID (RETAIL TRAP)</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 5. INTERACTIVE TOOL -->
                <div class="content-section">
                    <h3><i class='bx bx-calculator'></i> 5. VIP Interactive Tool: Market Structure & Institutional Bias Evaluator</h3>
                    <p>Input your multi-timeframe structural parameters to mathematically calculate your net institutional bias and generate strict execution clearances.</p>

                    <div class="tool-card" style="margin-top: 20px;">
                        <div class="tool-header">
                            <h4><i class='bx bx-stats'></i> Structural Bias Matrix Engine</h4>
                            <span class="badge-institutional">MODULE 2 ENGINE</span>
                        </div>

                        <div class="grid-2">
                            <div class="form-group">
                                <label><i class='bx bx-line-chart'></i> Higher Timeframe (Daily / H4) Trend</label>
                                <select id="m2HtfTrend">
                                    <option value="bullish">Bullish (Printing Higher Highs & BOS)</option>
                                    <option value="bearish">Bearish (Printing Lower Lows & BOS)</option>
                                    <option value="range">Consolidating / Ranging at Equilibrium</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-git-branch'></i> Medium Timeframe (H1 / M15) Event</label>
                                <select id="m2MtfEvent">
                                    <option value="choch_aligned">Fresh CHoCH in HTF Direction (+25 Pts)</option>
                                    <option value="bos_aligned">Clean BOS in HTF Direction (+20 Pts)</option>
                                    <option value="choch_counter">Counter-Trend CHoCH (Pullback Mode) (+5 Pts)</option>
                                    <option value="wick_sweep">Liquidity Sweep / SFP (+15 Pts)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-slider-alt'></i> Pricing Equilibrium (Discount / Premium)</label>
                                <select id="m2Pricing">
                                    <option value="ote">Deep OTE (62% - 79% Discount/Premium)</option>
                                    <option value="eq">Equilibrium (50% Zone)</option>
                                    <option value="expensive">Unfavorable (Buying Premium / Selling Discount)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label><i class='bx bx-shield-quarter'></i> Swing High / Low Defense</label>
                                <select id="m2Protection">
                                    <option value="strong">Testing Strong Protected Level</option>
                                    <option value="weak">Testing Weak Target Level</option>
                                </select>
                            </div>
                        </div>

                        <button class="calc-btn" onclick="evaluateMarketStructure()" style="margin-top: 15px;">
                            <i class='bx bx-analyse'></i> Calculate Institutional Bias
                        </button>

                        <div id="m2ResultContainer" class="calc-result" style="display: none; text-align: left; margin-top: 25px; padding: 25px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 12px; margin-bottom: 15px;">
                                <div class="label" style="font-size: 13px; font-weight: 700; color: #fff;">COMPUTED STRUCTURAL BIAS</div>
                                <div id="m2GradeBadge" class="badge-aaa">HIGH CONFIDENCE BULLISH</div>
                            </div>
                            <div class="value" id="m2BiasScore" style="text-align: center; font-size: 36px; margin: 15px 0;">95% Confluence</div>
                            <p id="m2Summary" style="font-size: 13px; line-height: 1.6; color: #ccc; margin-bottom: 15px;"></p>
                            <div id="m2Directive" style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; border-left: 3px solid var(--vip-gold); font-size: 13px; line-height: 1.6; color: #fff;"></div>
                        </div>
                    </div>
                </div>

                <!-- 6. VIP CHECKLIST -->
                <div class="content-section">
                    <h3><i class='bx bx-check-double'></i> 6. The VIP Institutional Structure Checklist</h3>
                    <p>7 non-negotiable rules for structure mapping before entering any position:</p>

                    <div class="sd-step-card">
                        <div class="sd-step-num">1</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Body Closes Only for BOS:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Never mark a structural break if only the wick penetrated the level. Wicks do the damage (sweeps); bodies tell the story (BOS).</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">2</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Identify the Dealing Range:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Locate the anchor swing low and swing high of the current active leg. Draw your 50% equilibrium before hunting entries.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">3</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Never Buy in Premium:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">No matter how bullish the chart looks, buying in Premium (>50%) drastically degrades your risk-reward ratio and exposes you to deep liquidity pullbacks.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">4</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Respect Strong Swing Highs/Lows:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Place your invalidation stop loss behind a verified Strong Protected swing point, not an arbitrary pip number.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">5</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Target Weak Highs/Lows as Liquidity:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Your Take Profit should be placed right at the doorstep of a Weak swing point that failed to break structure.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">6</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Align 3 Timeframe Tiers:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">Daily/H4 defines Narrative Bias; H1/M15 defines Key POIs; M5/M1 provides the Confirmation CHoCH trigger.</p>
                    </div>
                    <div class="sd-step-card">
                        <div class="sd-step-num">7</div>
                        <strong style="color: var(--vip-gold); font-size: 14px;">Wait for the Liquidity Sweep:</strong>
                        <p style="font-size: 13px; color: var(--vip-text-muted); margin-top: 4px;">A genuine CHoCH almost always occurs immediately after an opposing liquidity pool has been swept. No sweep = higher failure rate.</p>
                    </div>
                </div>

                <!-- 7. VIDEO MASTERCLASS -->
                <div class="yt-player-section">
                    <h3><i class='bx bxl-youtube' style="color:#FF0000"></i> Module 2 Masterclass: Market Structure & Smart Money Bias</h3>
                    <div class="yt-embed-wrapper">
                        <iframe src="https://www.youtube.com/embed/n4_8dFz-XyY?rel=0&modestbranding=1"
                            title="Market Structure & Smart Money Bias Masterclass"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen></iframe>
                    </div>
                    <div class="key-takeaways" style="margin-top: 20px;">
                        <h4>Masterclass Key Timestamps & Topics</h4>
                        <ul>
                            <li><strong>00:00 - 18:40:</strong> Advanced BOS vs CHoCH: The Body Close Rule & Wick Manipulation.</li>
                            <li><strong>18:41 - 36:15:</strong> Strong Protected vs Weak Target Highs & Lows.</li>
                            <li><strong>36:16 - 58:30:</strong> Premium vs Discount Fibonacci Arrays & Multi-Timeframe Alignment.</li>
                        </ul>
                    </div>
                </div>

                <!-- NAVIGATION -->
                <div class="content-nav">
                    <button class="nav-btn" onclick="showModule(1)"><i class='bx bx-left-arrow-alt'></i> Previous: Foundation</button>
                    <button class="nav-btn primary" onclick="showModule(3)">Next: Supply & Demand <i class='bx bx-right-arrow-alt'></i></button>
                </div>
            </div>
"""

print("Module 1 and Module 2 compiled.")
